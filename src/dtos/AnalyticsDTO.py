"""src/dtos/AnalyticsDTO.py

Data Transfer Objects cho phân hệ Phân tích bán hàng.
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import date


@dataclass
class DailyRevenueDTO:
    date: date
    revenue: float
    invoice_count: int
    day_label: str = ""  # Thứ 2, Thứ 3,...


@dataclass
class TopProductDTO:
    product_id: int
    product_name: str
    total_quantity: int
    total_revenue: float


@dataclass
class RevenueByPaymentDTO:
    payment_method: str
    total_revenue: float
    invoice_count: int


@dataclass
class RevenueByTimeSlotDTO:
    hour: int
    revenue: float


@dataclass
class CategorySalesDTO:
    category_name: str
    total_revenue: float
    percentage: float  # 0 - 100%


@dataclass
class AnalyticsDTO:
    period_label: str
    total_revenue: float
    revenue_growth: float  # e.g. 12.5 (%)
    total_invoices: int
    invoices_growth: float  # e.g. 8.2 (%)
    avg_order_value: float
    aov_growth: float  # e.g. -2.1 (%)
    returning_rate: float  # e.g. 42.8 (%)
    returning_growth: float  # e.g. 5.4 (%)
    total_profit: float
    daily_revenues: List[DailyRevenueDTO]
    top_products: List[TopProductDTO]
    categories: List[CategorySalesDTO]
    revenue_by_payment: List[RevenueByPaymentDTO]
    revenue_by_hour: List[RevenueByTimeSlotDTO]
