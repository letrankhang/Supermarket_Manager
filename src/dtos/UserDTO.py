from dataclasses import dataclass

@dataclass
class UserDTO:
    user_id: str
    full_name: str
    username: str
    role_name: str
    status: str