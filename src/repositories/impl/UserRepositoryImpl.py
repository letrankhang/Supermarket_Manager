import logging
from typing import List, Optional, Tuple
from sqlalchemy import or_
from sqlalchemy.orm import Session
from src.entities.user import User
from src.entities.role import Role
from src.repositories.UserRepository import UserRepository

logger = logging.getLogger(__name__)


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    # 1. HÀM CŨ: Dùng cho chức năng Đăng nhập
    def find_by_username(self, username: str) -> Optional[User]:
        try:
            return self.session.query(User).filter(User.username == username).first()
        except Exception as e:
            logger.error("Lỗi khi tìm user bằng username (%s): %s", username, e)
            raise e

    # 2. HÀM CŨ: Dùng cho chức năng Đổi mật khẩu / Quên mật khẩu
    def update_password_hash(self, user_id: int, password_hash: str) -> bool:
        try:
            user = self.session.query(User).filter(User.user_id == user_id).first()
            if user:
                user.password_hash = password_hash
                self.session.commit()
                return True

            if not user:
                return False
        except Exception as e:
            self.session.rollback()
            logger.error("Lỗi khi cập nhật mật khẩu (user_id=%d): %s", user_id, e)
            raise e

    def find_by_email(self, email: str) -> Optional[User]:
        try:
            return self.session.query(User).filter(User.email == email).first()
        except Exception as e:
            logger.error("Lỗi khi tìm user bằng email (%s): %s", email, e)
            raise e

    # 3. HÀM MỚI: Dùng cho màn hình Quản lý Nhân sự của bạn
    def find_users_with_roles(self, keyword: Optional[str] = None) -> List[Tuple[User, Role]]:
        try:
            query = self.session.query(User, Role).outerjoin(Role, User.role_id == Role.role_id)

            cleaned_keyword = (keyword or "").strip()
            if cleaned_keyword:
                pattern = f"%{cleaned_keyword}%"
                query = query.filter(
                    or_(
                        User.full_name.ilike(pattern),
                        User.username.ilike(pattern)
                    )
                )

            return query.order_by(User.full_name.asc()).all()
        except Exception as e:
            logger.error("Lỗi khi truy vấn users (keyword=%s): %s", keyword, e)
            raise e
