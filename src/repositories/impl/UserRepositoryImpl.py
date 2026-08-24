from typing import Optional

from sqlalchemy.orm import Session

from src.entities.user import User
from src.repositories.UserRepository import UserRepository

class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def find_by_username(self, username: str) -> Optional[User]:
        return self.session.query(User).filter(User.username == username).first()

    def find_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).first()

    def update_password_hash(self, user_id: int, password_hash: str) -> bool:
        user = self.session.query(User).filter(User.user_id == user_id).first()
        if not user:
            return False

        user.password_hash = password_hash
        self.session.commit()
        return True
