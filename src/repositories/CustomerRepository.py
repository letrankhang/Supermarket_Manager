from abc import ABC, abstractmethod
from typing import List, Optional

from src.entities.customer import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def find_customers(self, keyword: Optional[str] = None, limit: Optional[int] = None) -> List[Customer]:
        pass
