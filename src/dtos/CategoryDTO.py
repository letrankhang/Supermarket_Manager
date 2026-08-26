from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class CategoryDTO:
    category_id: Optional[int]
    category_name: str
    description: Optional[str]
    created_at: Optional[datetime] = None


@dataclass(frozen=True)
class CreateCategoryDTO:
    category_name: str
    description: Optional[str]


@dataclass(frozen=True)
class UpdateCategoryDTO:
    category_id: int
    category_name: str
    description: Optional[str]