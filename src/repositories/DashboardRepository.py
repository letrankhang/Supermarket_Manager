# File: D:\Python\Supermarket_Manager\src\repositories\DashboardRepository.py

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from src.entities.sales_invoice import SalesInvoice


class DashboardRepository(ABC):
    @abstractmethod
    def get_revenue_by_range(self, start_date: datetime, end_date: datetime) -> float:
        """
        Retrieves total revenue generated within a specific date range.
        """
        pass

    @abstractmethod
    def get_invoice_count_by_range(self, start_date: datetime, end_date: datetime) -> int:
        """
        Retrieves total invoice count within a specific date range.
        """
        pass

    @abstractmethod
    def get_low_stock_count(self, threshold: int) -> int:
        """
        Retrieves the count of products with stock level below or equal to the threshold.
        """
        pass

    @abstractmethod
    def get_customer_count_by_range(self, start_date: datetime, end_date: datetime) -> int:
        """
        Retrieves the count of customers created within a specific date range.
        """
        pass

    @abstractmethod
    def get_recent_invoices(self, limit: int = 5) -> List[SalesInvoice]:
        """
        Retrieves the most recent sales invoices up to the specified limit.
        """
        pass
