from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class RecentTransactionDTO:
    invoice_id: int
    invoice_code: str
    invoice_date: datetime
    formatted_time: str     
    final_total: float
    payment_method: str    


@dataclass
class DashboardDTO:
    today_revenue: float
    revenue_growth_rate: float      
    today_invoice_count: int
    invoice_growth_rate: float    
    low_stock_count: int           
    new_customer_count: int
    customer_growth_rate: float     
    weekly_revenue: List[float]    
    recent_transactions: List[RecentTransactionDTO]
