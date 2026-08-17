import os
from contextlib import contextmanager
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Load environment variables from .env file
load_dotenv()

class Database:
    """
    SQLAlchemy Connection Manager supporting Code-First auto-table creation
    for both MySQL and SQL Server.
    """
    _engine = None
    _sessionmaker = None
    _db_type = None

    @classmethod
    def _create_mysql_database_if_not_exists(cls, host, port, user, password, db_name):
        """Ensures the MySQL database exists before SQLAlchemy connects to it."""
        import mysql.connector
        try:
            connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password
            )
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            print(f"[Database Error] Could not verify/create MySQL database '{db_name}': {e}")
            raise e

    @classmethod
    def _create_mssql_database_if_not_exists(cls, server, port, user, password, db_name):
        """Ensures the SQL Server database exists before SQLAlchemy connects to it."""
        import pymssql
        try:
            connection = pymssql.connect(
                server=server,
                port=port,
                user=user,
                password=password,
                database="master"
            )
            connection.autocommit(True)
            cursor = connection.cursor()
            query = f"""
            IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'{db_name}')
            BEGIN
                CREATE DATABASE [{db_name}];
            END
            """
            cursor.execute(query)
            cursor.close()
            connection.close()
        except pymssql.Error as e:
            print(f"[Database Error] Could not verify/create SQL Server database '{db_name}': {e}")
            raise e

    @classmethod
    def initialize(cls):
        """Initializes the SQLAlchemy engine, session pool, and auto-generates tables."""
        if cls._engine is not None:
            return

        cls._db_type = os.getenv("DB_TYPE", "mysql").strip().lower()

        if cls._db_type == "mysql":
            db_host = os.getenv("DB_HOST", "localhost")
            db_port = int(os.getenv("DB_PORT", "3306"))
            db_user = os.getenv("DB_USER", "root")
            db_password = os.getenv("DB_PASSWORD", "")
            db_name = os.getenv("DB_NAME", "supermarket_db")

            # 1. Ensure the database exists
            cls._create_mysql_database_if_not_exists(db_host, db_port, db_user, db_password, db_name)

            # 2. Build SQLAlchemy connection string
            # Format: mysql+mysqlconnector://user:password@host:port/database
            connection_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
            
            # 3. Create the Engine
            cls._engine = create_engine(
                connection_url,
                pool_recycle=3600,
                pool_pre_ping=True
            )
            print(f"[Database] SQLAlchemy MySQL engine initialized successfully for '{db_name}'.")

        elif cls._db_type == "mssql":
            server = os.getenv("MSSQL_SERVER", "localhost")
            port = int(os.getenv("MSSQL_PORT", "1433"))
            user = os.getenv("MSSQL_USER", "sa")
            password = os.getenv("MSSQL_PASSWORD", "")
            db_name = os.getenv("MSSQL_NAME", "supermarket_db")

            # 1. Ensure the database exists
            cls._create_mssql_database_if_not_exists(server, port, user, password, db_name)

            # 2. Build SQLAlchemy connection string
            # Format: mssql+pymssql://user:password@host:port/database
            connection_url = f"mssql+pymssql://{user}:{password}@{server}:{port}/{db_name}"

            # 3. Create the Engine
            cls._engine = create_engine(
                connection_url,
                pool_pre_ping=True
            )
            print(f"[Database] SQLAlchemy SQL Server engine initialized successfully for '{db_name}'.")
        else:
            raise ValueError(f"Unsupported DB_TYPE: {cls._db_type}. Use 'mysql' or 'mssql'.")

        # 4. Bind sessionmaker (scoped session for thread safety)
        session_factory = sessionmaker(bind=cls._engine)
        cls._sessionmaker = scoped_session(session_factory)

        # 5. Code-First Auto-Table Generation
        from src.entities import (
            Base, Role, User, Category, Product, Supplier, SupplierProduct,
            ImportOrder, ImportDetail, CustomerTier, Customer, SalesInvoice, SalesDetail
        )


        try:
            Base.metadata.create_all(cls._engine)
            print("[Database] Code-First tables generated/verified successfully.")

            # Automatically add missing 'image' column to 'products' table if needed
            from sqlalchemy import inspect, text
            inspector = inspect(cls._engine)
            if 'products' in inspector.get_table_names():
                columns = [col['name'] for col in inspector.get_columns('products')]
                if 'image' not in columns:
                    print("[Database] Adding missing 'image' column to 'products' table...")
                    with cls._engine.connect() as conn:
                        conn.execute(text("ALTER TABLE products ADD image VARCHAR(500) NULL"))
                        conn.commit()
                    print("[Database] 'image' column added successfully.")

            # Automatically add missing 'email' column to 'users' table if needed
            if 'users' in inspector.get_table_names():
                columns = [col['name'] for col in inspector.get_columns('users')]
                if 'email' not in columns:
                    print("[Database] Adding missing 'email' column to 'users' table...")
                    with cls._engine.connect() as conn:
                        conn.execute(text("ALTER TABLE users ADD email VARCHAR(100) NULL"))
                        conn.commit()
                    print("[Database] 'email' column added successfully.")

            # --- Database Auto-Seeding ---
            with cls.get_session_ctx() as session:
                # 1. Seed Roles
                default_roles = ["Admin", "Manager", "Cashier"]
                existing_roles = {r.role_name: r for r in session.query(Role).all()}
                
                db_roles = {}
                for role_name in default_roles:
                    if role_name not in existing_roles:
                        new_role = Role(role_name=role_name)
                        session.add(new_role)
                        session.flush()  # to obtain auto-incremented role_id
                        db_roles[role_name] = new_role
                        print(f"[Database Seed] Role '{role_name}' created successfully.")
                    else:
                        db_roles[role_name] = existing_roles[role_name]

                # 2. Seed Default Admin User
                admin_role = db_roles.get("Admin")
                if admin_role:
                    admin_user = session.query(User).filter_by(username="admin").first()
                    if not admin_user:
                        new_admin = User(
                            username="admin",
                            password_hash="admin",
                            full_name="Administrator",
                            role_id=admin_role.role_id,
                            email="admin@supermarket.com",
                            is_active=True
                        )
                        session.add(new_admin)
                        print("[Database Seed] Default Admin user created successfully (username: 'admin', password: 'admin', email: 'admin@supermarket.com').")
                    else:
                        if not admin_user.email:
                            admin_user.email = "admin@supermarket.com"
                            print("[Database Seed] Assigned default email 'admin@supermarket.com' to existing admin user.")
                        # Di trú mật khẩu cũ từ dạng hash sang dạng text thường
                        import hashlib
                        old_hash = hashlib.sha256("admin".encode('utf-8')).hexdigest()
                        if admin_user.password_hash == old_hash:
                            admin_user.password_hash = "admin"
                            print("[Database Seed] Updated existing admin user's password from hash to plain text.")
        except Exception as e:
            print(f"[Database Error] Failed to generate database tables or seed data: {e}")
            raise e

    @classmethod
    def get_engine(cls):
        """Returns the raw SQLAlchemy engine."""
        if cls._engine is None:
            cls.initialize()
        return cls._engine

    @classmethod
    @contextmanager
    def get_session_ctx(cls):
        """
        Context manager that yields a SQLAlchemy Session.
        Handles commits, rollbacks, and connection clean up automatically.
        
        Usage:
            with Database.get_session_ctx() as session:
                products = session.query(Product).all()
        """
        if cls._sessionmaker is None:
            cls.initialize()
            
        session = cls._sessionmaker()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"[Database Session Error] Transaction failed, rolling back changes: {e}")
            raise e
        finally:
            session.close()
