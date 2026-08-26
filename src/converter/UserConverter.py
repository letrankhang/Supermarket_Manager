from typing import Optional
from src.dtos.UserDTO import UserDTO
from src.entities.user import User
from src.entities.role import Role


class UserConverter:
    @staticmethod
    def to_dto(user: User, role: Optional[Role]) -> UserDTO:
        role_name = role.role_name if role else "N/A"

        status_text = "Active" if user.is_active else "Inactive"

        return UserDTO(
            user_id=str(user.user_id),
            full_name=user.full_name or "",
            username=user.username or "",
            role_name=role_name,
            status=status_text
        )