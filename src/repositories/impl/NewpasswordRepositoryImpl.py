from sqlalchemy.orm import Session
from src.entities.user import User
from src.repositories.NewpasswordRepository import NewpasswordRepository

class NewpasswordRepositoryImpl(NewpasswordRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def update_password(self, email: str, new_password_plain: str) -> bool:
        user = self.session.query(User).filter(User.email == email).first()
        if user:
            user.password_hash = new_password_plain
            self.session.commit()
            return True
        return False
