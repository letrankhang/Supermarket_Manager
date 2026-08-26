import logging
from datetime import datetime
from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Session

from src.entities.sales_invoice import SalesInvoice
from src.entities.product import Product
from src.entities.customer import Customer
from src.repositories.DashboardRepository import DashboardRepository

logger = logging.getLogger(__name__)

class DashboardRepositoryImpl(DashboardRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_revenue_by_range(self, start_date: datetime, end_date: datetime) -> float:
        try:
            query_val = self.session.query(func.sum(SalesInvoice.final_total))\
                .filter(SalesInvoice.invoice_date >= start_date, SalesInvoice.invoice_date <= end_date).scalar()
            return float(query_val) if query_val is not None else 0.0
        except Exception as e:
            logger.error("Error querying revenue by range [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_invoice_count_by_range(self, start_date: datetime, end_date: datetime) -> int:
        try:
            query_val = self.session.query(func.count(SalesInvoice.invoice_id))\
                .filter(SalesInvoice.invoice_date >= start_date, SalesInvoice.invoice_date <= end_date).scalar()
            return int(query_val) if query_val is not None else 0
        except Exception as e:
            logger.error("Error querying invoice count by range [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_low_stock_count(self, threshold: int) -> int:
        try:
            query_val = self.session.query(func.count(Product.product_id))\
                .filter(Product.current_stock <= threshold).scalar()
            return int(query_val) if query_val is not None else 0
        except Exception as e:
            logger.error("Error querying low stock count with threshold %d: %s", threshold, e)
            raise e


    def get_customer_count_by_range(self, start_date: datetime, end_date: datetime) -> int:
        try:
            query_val = self.session.query(func.count(Customer.customer_id))\
                .filter(Customer.created_at >= start_date, Customer.created_at <= end_date).scalar()
            return int(query_val) if query_val is not None else 0
        except Exception as e:
            logger.error("Error querying customer count by range [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_recent_invoices(self, limit: int = 5) -> List[SalesInvoice]:
        try:
            return self.session.query(SalesInvoice)\
                .order_by(SalesInvoice.invoice_date.desc())\
                .limit(limit)\
                .all()
        except Exception as e:
            logger.error("Error querying recent invoices (limit=%d): %s", limit, e)
            raise e
