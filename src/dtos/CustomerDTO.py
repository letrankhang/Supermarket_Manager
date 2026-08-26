from dataclasses import dataclass
from typing import Optional

@dataclass
class CustomerDTO:
    customer_id: int
    full_name: str
    phone: str

    @property
    def display_name(self) -> str:
        return self.full_name or self.phone
