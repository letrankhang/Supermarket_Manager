from abc import ABC, abstractmethod
from src.dtos.AnalyticsDTO import AnalyticsDTO

class AnalyticsService(ABC):
    @abstractmethod
    def get_analytics_by_period(self, period_type: str = "week") -> AnalyticsDTO:
        pass
