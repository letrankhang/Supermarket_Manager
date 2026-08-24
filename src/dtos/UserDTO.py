"""DTO người dùng dùng cho màn hình Quản lý nhân sự."""
from dataclasses import dataclass

@dataclass
class UserDTO:
    """Một nhân viên hiển thị trên bảng dữ liệu."""
    user_id: str
    full_name: str
    username: str
    role_name: str
    status: str