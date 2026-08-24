from typing import Optional
from src.dtos.UserDTO import UserDTO
from src.entities.user import User
from src.entities.role import Role


class UserConverter:
    @staticmethod
    def to_dto(user: User, role: Optional[Role]) -> UserDTO:
        """Đổi thông tin từ bảng User và Role thành UserDTO."""

        # Nếu có Role thì lấy role_name, không thì hiển thị N/A
        ten_vai_tro = role.role_name if role else "N/A"

        # is_active là Boolean (True/False) -> Đổi thành String (Active/Inactive)
        trang_thai = "Active" if user.is_active else "Inactive"

        return UserDTO(
            user_id=str(user.user_id),
            full_name=user.full_name or "",
            username=user.username or "",
            role_name=ten_vai_tro,
            status=trang_thai
        )