from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from datetime import date

from src.entities.customer import Customer
from src.entities.customer_tier import CustomerTier


class CustomerManagementRepository(ABC):
    @abstractmethod
    def find_all_customers(self, keyword: Optional[str] = None, tier_id: Optional[int] = None, limit: Optional[int] = None) -> List[Customer]:
        pass

    @abstractmethod
    def find_customer_by_id(self, customer_id: int) -> Optional[Customer]:
        pass

    @abstractmethod
    def find_customer_by_phone(self, phone: str) -> Optional[Customer]:
        pass

    @abstractmethod
    def count_customers(self) -> int:
        pass

    @abstractmethod
    def count_customers_by_tier(self) -> List[Tuple[str, int]]:
        pass

    @abstractmethod
    def insert_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def update_customer(self, customer_id: int, phone: str, full_name: str, dob: Optional[date]) -> None:
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def get_all_tiers(self) -> List[CustomerTier]:
        pass
