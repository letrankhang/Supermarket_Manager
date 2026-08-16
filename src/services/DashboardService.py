# File: D:\Python\Supermarket_Manager\src\services\DashboardService.py

from abc import ABC, abstractmethod
from src.dtos.DashboardDTO import DashboardDTO


class DashboardService(ABC):
    """
    Service interface for retrieving system dashboard data.
    """

    @abstractmethod
    def get_dashboard_data(self, low_stock_threshold: int = 10) -> DashboardDTO:
        pass
