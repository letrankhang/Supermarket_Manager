from sqlalchemy.orm import Session
from typing import Optional
from src.entities.user import User
from src.repositories.LoginRepository import LoginRepository


class LoginRepositotyImpl(LoginRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def find_by_username(self, username: str) -> Optional[User]:
        return self.session.query(User).filter(User.username == username).first()
