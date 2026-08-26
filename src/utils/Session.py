import logging
from typing import Optional


logger = logging.getLogger(__name__)

class Session:
    _user_id: Optional[int] = None
    _username: Optional[str] = None
    _full_name: Optional[str] = None
    _role_name: Optional[str] = None


    @classmethod
    def start_session(cls, user_id: int, username: str, role_name: str,
                      full_name: Optional[str] = None):
        cls._user_id = user_id
        cls._username = username
        cls._full_name = full_name
        cls._role_name = role_name
        logger.info( "Session started: user_id=%d, username='%s', role='%s'", user_id, username, role_name)

    
    @classmethod
    def clear_session(cls):
        if cls._user_id is not None:
            logger.info("Session cleared for user_id=%d, username='%s'", cls._user_id, cls._username)
        
        cls._user_id = None
        cls._username = None
        cls._full_name = None
        cls._role_name = None


    @classmethod
    def is_active(cls) -> bool:
        return cls._user_id is not None


    @classmethod
    def get_user_id(cls) -> Optional[int]:
        return cls._user_id


    @classmethod
    def get_username(cls) -> Optional[str]:
        return cls._username


    @classmethod
    def get_full_name(cls) -> Optional[str]:
        return cls._full_name or cls._username


    @classmethod
    def get_role_name(cls) -> Optional[str]:
        return cls._role_name
