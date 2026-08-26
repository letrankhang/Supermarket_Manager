from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import date, datetime

@dataclass
class CustomerDetailDTO:
    customer_id: int
    phone: str
    full_name: str
    dob: Optional[date]
    total_points: int
    total_spent: float
    tier_name: str
    discount_percent: int
    created_at: Optional[datetime]


@dataclass
class CustomerManagementDTO:
    customers: List[CustomerDetailDTO]
    total_count: int
    tier_summary: Dict[str, int]


@dataclass
class CustomerFormDTO:
    phone: str
    full_name: str
    dob: Optional[date]
