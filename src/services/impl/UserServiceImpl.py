import logging
from typing import List, Optional, Dict, Tuple

from config.database import Database
from src.dtos.UserDTO import UserDTO
from src.repositories.impl.UserRepositoryImpl import UserRepositoryImpl
from src.services.UserService import UserService
from src.converter.UserConverter import UserConverter

logger = logging.getLogger(__name__)


class UserServiceImpl(UserService):
    def get_personnel_dashboard(self, keyword: Optional[str] = None) -> Tuple[List[UserDTO], int, int, Dict[str, int]]:
        with Database.get_session_ctx() as session:
            repository = UserRepositoryImpl(session)
            user_role_pairs = repository.find_users_with_roles(keyword=keyword)

            danh_sach = []
            active_count = 0
            roles_count = {"Admin": 0, "Cashier": 0, "Warehouse": 0}

            for user, role in user_role_pairs:
                # 1. Chuyển sang DTO
                dto = UserConverter.to_dto(user, role)
                danh_sach.append(dto)

                # 2. Đếm số lượng Active
                if dto.status == "Active":
                    active_count += 1

                # 3. Đếm phân bổ vai trò
                if dto.role_name in roles_count:
                    roles_count[dto.role_name] += 1
                else:
                    roles_count[dto.role_name] = 1

            total_count = len(user_role_pairs)

        logger.info("Tải Dashboard nhân sự: %d kết quả.", total_count)
        return danh_sach, total_count, active_count, roles_count

    def add_user(self, data: dict) -> bool:
        """Thêm nhân viên mới vào cơ sở dữ liệu."""
        from src.entities.user import User
        from src.entities.role import Role
        import bcrypt

        try:
            with Database.get_session_ctx() as session:
                # 1. Tìm Role ID từ tên chức vụ (Admin, Cashier, Warehouse...)
                role_name = data.get('role_name')
                role = session.query(Role).filter(Role.role_name == role_name).first()
                if not role and role_name:
                    # Nếu Role chưa có trong Database, tự động tạo mới
                    role = Role(role_name=role_name)
                    session.add(role)
                    session.flush()

                if not role:
                    logger.error("Không tìm thấy hoặc không thể tạo vai trò: %s", role_name)
                    return False

                role_id = role.role_id

                # 2. Mã hóa mật khẩu chuẩn bcrypt
                raw_password = data.get('password', '123456').encode('utf-8')
                hashed_password = bcrypt.hashpw(raw_password, bcrypt.gensalt()).decode('utf-8')

                # 3. Tạo dữ liệu mới
                new_user = User(
                    username=data.get('username'),
                    full_name=data.get('full_name'),
                    email=data.get('email'),
                    password_hash=hashed_password,
                    role_id=role_id,
                    is_active=True
                )

                # 4. LƯU VÀO DATABASE
                session.add(new_user)
                session.commit()
                return True
        except Exception as e:
            logger.error("Lỗi khi thêm nhân viên: %s", e)
            return False

    def update_user(self, username: str, data: dict) -> bool:
        """Cập nhật nhân viên trong cơ sở dữ liệu."""
        from src.entities.user import User
        from src.entities.role import Role
        import bcrypt

        try:
            with Database.get_session_ctx() as session:
                user = session.query(User).filter(User.username == username).first()
                if not user:
                    return False

                user.full_name = data.get('full_name')
                user.email = data.get('email')
                user.is_active = True if data.get('status') == 'Active' else False

                role_name = data.get('role_name')
                if role_name:
                    role = session.query(Role).filter(Role.role_name == role_name).first()
                    if not role:
                        role = Role(role_name=role_name)
                        session.add(role)
                        session.flush()
                    user.role_id = role.role_id

                new_password = data.get('password')
                if new_password:  # Nếu có nhập mật khẩu mới thì mới đổi
                    user.password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

                # LƯU VÀO DATABASE
                session.commit()
                return True
        except Exception as e:
            logger.error("Lỗi khi sửa nhân viên: %s", e)
            return False

    def delete_user(self, user_id: str) -> bool:
        """Xóa vĩnh viễn nhân viên khỏi Database."""
        from src.entities.user import User
        import logging
        logger = logging.getLogger(__name__)

        try:
            with Database.get_session_ctx() as session:
                user = session.query(User).filter(User.user_id == int(user_id)).first()
                if user:
                    session.delete(user)
                    session.commit()
                    return True
                return False
        except Exception as e:
            logger.error("Lỗi khi xóa nhân viên: %s", e)
            return False