from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session

from src.entities.category import Category


class CategoryRepository(ABC):

    @abstractmethod
    def get_by_id(self, session: Session, category_id: int) -> Optional[Category]:
        pass

    @abstractmethod
    def get_by_name(self, session: Session, category_name: str) -> Optional[Category]:
        pass

    @abstractmethod
    def list_all(self, session: Session) -> List[Category]:
        pass

    @abstractmethod
    def create(self, session: Session, category: Category) -> Category:
        pass

    @abstractmethod
    def update(self, session: Session, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, session: Session, category_id: int) -> bool:
        pass