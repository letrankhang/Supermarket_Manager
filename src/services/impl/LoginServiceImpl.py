import hashlib
import logging
from typing import Optional
from sqlalchemy.orm import make_transient
from config.database import Database
from src.entities.user import User
from src.entities.role import Role
from src.services.LoginService import LoginService
from src.repositories.impl.UserRepositoryImpl import UserRepositoryImpl
from src.utils.PasswordHasher import verify_password
from src.utils.Session import Session as UserSession

logger = logging.getLogger(__name__)


class LoginServiceImpl(LoginService):
    def login(self, username: str, password: str) -> Optional[User]:
        try:
            with Database.get_session_ctx() as db_session:
                repo = UserRepositoryImpl(db_session)
                user = repo.find_by_username(username)
                
                if not user:
                    logger.warning("Đăng nhập thất bại: Không tìm thấy tài khoản '%s'.", username)
                    return None

                if not user.is_active:
                    logger.warning("Đăng nhập thất bại: Tài khoản '%s' đã bị khóa.", username)
                    return None

                if not verify_password(password, user.password_hash):
                    logger.warning("Đăng nhập thất bại: Mật khẩu không chính xác cho tài khoản '%s'.", username)
                    return None

                role = db_session.query(Role).filter_by(role_id=user.role_id).first()
                role_name = role.role_name if role else "User"

                UserSession.start_session(user.user_id, user.username, role_name)

                make_transient(user)

                logger.info("Người dùng '%s' đăng nhập thành công với vai trò '%s'.", username, role_name)
                return user
        except Exception as e:
            logger.error("Lỗi xảy ra trong quá trình đăng nhập cho tài khoản '%s': %s", username, e)
            raise e