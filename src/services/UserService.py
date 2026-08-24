from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Tuple
from src.dtos.UserDTO import UserDTO

class UserService(ABC):
    @abstractmethod
    def get_personnel_dashboard(self, keyword: Optional[str] = None) -> Tuple[List[UserDTO], int, int, Dict[str, int]]:
        """Lấy danh sách DTO và các số liệu thống kê."""
        pass