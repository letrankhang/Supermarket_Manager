from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass
class DailyRevenueDTO:
    date: date
    revenue: float
    invoice_count: int
    day_label: str = "" 

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
    percentage: float  


@dataclass
class AnalyticsDTO:
    period_label: str
    total_revenue: float
    revenue_growth: float  
    total_invoices: int
    invoices_growth: float  
    avg_order_value: float
    aov_growth: float 
    returning_rate: float  
    returning_growth: float  
    total_profit: float
    daily_revenues: List[DailyRevenueDTO]
    top_products: List[TopProductDTO]
    categories: List[CategorySalesDTO]
    revenue_by_payment: List[RevenueByPaymentDTO]
    revenue_by_hour: List[RevenueByTimeSlotDTO]
