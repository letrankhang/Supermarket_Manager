from abc import ABC, abstractmethod
from src.dtos.AnalyticsDTO import AnalyticsDTO


class AnalyticsService(ABC):
    @abstractmethod
    def get_analytics_data(self, year: int, month: int) -> AnalyticsDTO:
        pass

    @abstractmethod
    def get_analytics_by_period(self, period_type: str = "week") -> AnalyticsDTO:
        """Lấy dữ liệu phân tích theo 'today', 'week', hoặc 'month'."""
        pass
