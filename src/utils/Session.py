# File: D:\Python\Supermarket_Manager\src\utils\Sesion.py

import logging
from typing import Optional

# Khởi tạo logger cho class Session
logger = logging.getLogger(__name__)


class Session:
    """
    Lớp quản lý phiên làm việc của người dùng (Session Management).
    Áp dụng mẫu thiết kế tĩnh (Static Class) để dễ dàng truy cập thông tin phiên từ mọi nơi trong ứng dụng.
    """
    _user_id: Optional[int] = None
    _username: Optional[str] = None
    _role_name: Optional[str] = None

    @classmethod
    def start_session(cls, user_id: int, username: str, role_name: str) -> None:
        """
        Khởi tạo phiên làm việc mới cho người dùng sau khi đăng nhập thành công.

        Args:
            user_id (int): ID của người dùng.
            username (str): Tên đăng nhập.
            role_name (str): Tên vai trò (ví dụ: Admin, Manager, Cashier).
        """
        cls._user_id = user_id
        cls._username = username
        cls._role_name = role_name
        logger.info( "Session started: user_id=%d, username='%s', role='%s'", user_id, username, role_name)
    
    @classmethod
    def clear_session(cls) -> None:
        """
        Xóa phiên làm việc hiện tại khi người dùng đăng xuất hoặc phiên hết hạn.
        """
        if cls._user_id is not None:
            logger.info("Session cleared for user_id=%d, username='%s'", cls._user_id, cls._username)
        
        cls._user_id = None
        cls._username = None
        cls._role_name = None

    @classmethod
    def is_active(cls) -> bool:
        """
        Kiểm tra xem phiên làm việc có đang hoạt động (đã đăng nhập) hay không.

        Returns:
            bool: True nếu có phiên hoạt động, ngược lại False.
        """
        return cls._user_id is not None

    @classmethod
    def get_user_id(cls) -> Optional[int]:
        """
        Lấy ID của người dùng đang đăng nhập.

        Returns:
            Optional[int]: ID người dùng hoặc None nếu chưa đăng nhập.
        """
        return cls._user_id

    @classmethod
    def get_username(cls) -> Optional[str]:
        """
        Lấy tên đăng nhập của người dùng.

        Returns:
            Optional[str]: Tên đăng nhập hoặc None.
        """
        return cls._username

    @classmethod
    def get_role_name(cls) -> Optional[str]:
        """
        Lấy vai trò của người dùng.

        Returns:
            Optional[str]: Tên vai trò hoặc None.
        """
        return cls._role_name
