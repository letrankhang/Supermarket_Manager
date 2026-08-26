from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from src.entities.sales_invoice import SalesInvoice


class DashboardRepository(ABC):
    @abstractmethod
    def get_revenue_by_range(self, start_date: datetime, end_date: datetime) -> float:
        pass

    @abstractmethod
    def get_invoice_count_by_range(self, start_date: datetime, end_date: datetime) -> int:
        pass

    @abstractmethod
    def get_low_stock_count(self, threshold: int) -> int:
        pass

    @abstractmethod
    def get_customer_count_by_range(self, start_date: datetime, end_date: datetime) -> int:
        pass

    @abstractmethod
    def get_recent_invoices(self, limit: int = 5) -> List[SalesInvoice]:
        pass
