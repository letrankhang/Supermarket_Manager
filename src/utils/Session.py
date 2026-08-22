import logging
from typing import Optional

logger = logging.getLogger(__name__)


class Session:
    """Quản lý phiên đăng nhập, để mọi nơi trong ứng dụng đọc được thông tin người dùng."""
    _user_id: Optional[int] = None
    _username: Optional[str] = None
    _role_name: Optional[str] = None

    @classmethod
    def start_session(cls, user_id: int, username: str, role_name: str) -> None:
        """Mở phiên làm việc mới sau khi đăng nhập thành công."""
        cls._user_id = user_id
        cls._username = username
        cls._role_name = role_name
        logger.info( "Session started: user_id=%d, username='%s', role='%s'", user_id, username, role_name)
    
    @classmethod
    def clear_session(cls) -> None:
        """Xóa phiên hiện tại khi đăng xuất hoặc phiên hết hạn."""
        if cls._user_id is not None:
            logger.info("Session cleared for user_id=%d, username='%s'", cls._user_id, cls._username)
        
        cls._user_id = None
        cls._username = None
        cls._role_name = None

    @classmethod
    def is_active(cls) -> bool:
        """Cho biết đang có phiên đăng nhập hay không."""
        return cls._user_id is not None

    @classmethod
    def get_user_id(cls) -> Optional[int]:
        """Lấy ID người dùng đang đăng nhập."""
        return cls._user_id

    @classmethod
    def get_username(cls) -> Optional[str]:
        """Lấy tên đăng nhập của người dùng."""
        return cls._username

    @classmethod
    def get_role_name(cls) -> Optional[str]:
        """Lấy vai trò của người dùng."""
        return cls._role_name
