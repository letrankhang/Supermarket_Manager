from sqlalchemy.orm import Session
from typing import Optional
from src.entities.user import User
from src.repositories.ForgotpasswordRepository import ForgotpasswordRepository


class ForgotpasswordRepositoryImpl(ForgotpasswordRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def find_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).first()
