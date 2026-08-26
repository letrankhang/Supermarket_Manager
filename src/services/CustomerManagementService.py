from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.dtos.CustomerManagementDTO import CustomerManagementDTO, CustomerFormDTO, CustomerDetailDTO

class CustomerManagementService(ABC):
    @abstractmethod
    def get_customers(self, keyword: Optional[str] = None, tier_id: Optional[int] = None) -> CustomerManagementDTO:
        pass

    @abstractmethod
    def add_customer(self, form: CustomerFormDTO) -> CustomerDetailDTO:
        pass

    @abstractmethod
    def update_customer(self, customer_id: int, form: CustomerFormDTO) -> None:
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def get_tiers(self) -> List[Tuple[int, str]]:
        pass
