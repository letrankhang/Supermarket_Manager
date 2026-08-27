from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session

from src.entities.import_order import ImportOrder


class ImportRepository(ABC):
    @abstractmethod
    def create(self, session: Session, order: ImportOrder) -> ImportOrder:
        pass

    @abstractmethod
    def get_by_id(self, session: Session, import_id: int) -> Optional[ImportOrder]:
        pass

    @abstractmethod
    def list_all(self, session: Session) -> List[ImportOrder]:
        pass