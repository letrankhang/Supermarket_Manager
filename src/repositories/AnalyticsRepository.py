from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Tuple, Any


class AnalyticsRepository(ABC):
    @abstractmethod
    def get_daily_revenue(self, start_date: datetime, end_date: datetime) -> List[Tuple[Any, float, int]]:
        pass

    @abstractmethod
    def get_total_revenue(self, start_date: datetime, end_date: datetime) -> float:
        pass

    @abstractmethod
    def get_total_profit(self, start_date: datetime, end_date: datetime) -> float:
        pass

    @abstractmethod
    def get_invoice_count(self, start_date: datetime, end_date: datetime) -> int:
        pass

    @abstractmethod
    def get_top_products(self, start_date: datetime, end_date: datetime, limit: int) -> List[Tuple[int, str, int, float]]:
        pass

    @abstractmethod
    def get_category_sales(self, start_date: datetime, end_date: datetime) -> List[Tuple[str, float]]:
        pass

    @abstractmethod
    def get_revenue_by_payment_method(self, start_date: datetime, end_date: datetime) -> List[Tuple[str, float, int]]:
        pass

    @abstractmethod
    def get_revenue_by_hour(self, start_date: datetime, end_date: datetime) -> List[Tuple[int, float]]:
        pass
