# File: D:\Python\Supermarket_Manager\src\dtos\DashboardDTO.py

from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class RecentTransactionDTO:
    """
    Data Transfer Object representing a single recent sales transaction.
    """
    invoice_id: int
    invoice_code: str
    invoice_date: datetime
    formatted_time: str     # E.g. "10:45 AM", "Hôm qua", "16/08/2026"
    final_total: float
    payment_method: str     # Nhãn tiếng Việt: "Tiền mặt" / "Chuyển khoản" / "Thẻ" 


@dataclass
class DashboardDTO:
    """
    Data Transfer Object holding all aggregated metrics for the system dashboard.
    """
    today_revenue: float
    revenue_growth_rate: float      # Revenue comparison with yesterday in %
    today_invoice_count: int
    invoice_growth_rate: float      # Invoice count comparison with yesterday in %
    low_stock_count: int            # Products with stock <= warning threshold
    new_customer_count: int
    customer_growth_rate: float     # Customer registration comparison with yesterday in %
    weekly_revenue: List[float]     # Revenues for weeks of the current month (typically 4 weeks)
    recent_transactions: List[RecentTransactionDTO]
