from abc import ABC, abstractmethod
from typing import List

from src.dtos.DashboardDTO import DashboardDTO

class DashboardService(ABC):
    @abstractmethod
    def get_dashboard_data(self, low_stock_threshold: int = 10) -> DashboardDTO:
        pass

    @abstractmethod
    def get_weekly_revenue(self, year: int, month: int) -> List[float]:
        pass
