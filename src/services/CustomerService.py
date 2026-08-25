from abc import ABC, abstractmethod
from typing import List, Optional

from src.dtos.CustomerDTO import CustomerDTO

class CustomerService(ABC):
    @abstractmethod
    def search_customers(self, keyword: Optional[str] = None) -> List[CustomerDTO]:
        pass
