import logging
from datetime import datetime
from typing import Any, List, Tuple

from sqlalchemy import Date, cast, extract, func
from sqlalchemy.orm import Session

from src.entities.category import Category
from src.entities.product import Product
from src.entities.sales_detail import SalesDetail
from src.entities.sales_invoice import SalesInvoice
from src.repositories.AnalyticsRepository import AnalyticsRepository

logger = logging.getLogger(__name__)


class AnalyticsRepositoryImpl(AnalyticsRepository):
    def __init__(self, session: Session) -> None:
        self.session = session


    def get_daily_revenue(self, start_date: datetime, end_date: datetime) -> List[Tuple[Any, float, int]]:
        try:
            dialect_name = ""
            if self.session.bind:
                dialect_name = getattr(self.session.bind.dialect, "name", "").lower()

            if dialect_name == "mssql":
                date_col = cast(SalesInvoice.invoice_date, Date)
            else:
                date_col = func.date(SalesInvoice.invoice_date)

            results = (
                self.session.query(
                    date_col.label("inv_date"),
                    func.sum(SalesInvoice.final_total).label("revenue"),
                    func.count(SalesInvoice.invoice_id).label("invoice_count"),
                )
                .filter(
                    SalesInvoice.invoice_date >= start_date,
                    SalesInvoice.invoice_date <= end_date,
                )
                .group_by(date_col)
                .order_by(date_col.asc())
                .all()
            )
            return [
                (
                    row[0],
                    float(row[1] if row[1] is not None else 0.0),
                    int(row[2] if row[2] is not None else 0),
                )
                for row in results
            ]
        except Exception as e:
            logger.error("Lỗi khi truy vấn doanh thu theo ngày [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_total_revenue(self, start_date: datetime, end_date: datetime) -> float:
        try:
            val = (
                self.session.query(func.sum(SalesInvoice.final_total))
                .filter(
                    SalesInvoice.invoice_date >= start_date,
                    SalesInvoice.invoice_date <= end_date,
                )
                .scalar()
            )
            return float(val or 0.0)
        except Exception as e:
            logger.error("Lỗi khi truy vấn tổng doanh thu [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_total_profit(self, start_date: datetime, end_date: datetime) -> float:
        try:
            val = (
                self.session.query(
                    func.sum((SalesDetail.unit_price - SalesDetail.cost_price) * SalesDetail.quantity)
                )
                .join(SalesInvoice, SalesDetail.invoice_id == SalesInvoice.invoice_id)
                .filter(
                    SalesInvoice.invoice_date >= start_date,
                    SalesInvoice.invoice_date <= end_date,
                )
                .scalar()
            )
            return float(val or 0.0)
        except Exception as e:
            logger.error("Lỗi khi truy vấn tổng lợi nhuận [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_invoice_count(self, start_date: datetime, end_date: datetime) -> int:
        try:
            val = (
                self.session.query(func.count(SalesInvoice.invoice_id))
                .filter(
                    SalesInvoice.invoice_date >= start_date,
                    SalesInvoice.invoice_date <= end_date,
                )
                .scalar()
            )
            return int(val or 0)
        except Exception as e:
            logger.error("Lỗi khi truy vấn số lượng hóa đơn [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_top_products(
        self, start_date: datetime, end_date: datetime, limit: int = 5
    ) -> List[Tuple[int, str, int, float]]:
        try:
            results = (
                self.session.query(
                    Product.product_id,
                    Product.product_name,
                    func.sum(SalesDetail.quantity).label("total_qty"),
                    func.sum(SalesDetail.unit_price * SalesDetail.quantity).label("total_rev"),
                )
                .join(SalesDetail, Product.product_id == SalesDetail.product_id)
                .join(SalesInvoice, SalesDetail.invoice_id == SalesInvoice.invoice_id)
                .filter(
                    SalesInvoice.invoice_date >= start_date,
                    SalesInvoice.invoice_date <= end_date,
                )
                .group_by(Product.product_id, Product.product_name)
                .order_by(func.sum(SalesDetail.quantity).desc())
                .limit(limit)
                .all()
            )
            return [
                (
                    int(row[0]),
                    str(row[1]),
                    int(row[2] if row[2] is not None else 0),
                    float(row[3] if row[3] is not None else 0.0),
                )
                for row in results
            ]
        except Exception as e:
            logger.error("Lỗi khi truy vấn top sản phẩm [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_category_sales(self, start_date: datetime, end_date: datetime) -> List[Tuple[str, float]]:
        try:
            results = (
                self.session.query(
                    Category.category_name,
                    func.sum(SalesDetail.unit_price * SalesDetail.quantity).label("cat_rev"),
                )
                .join(Product, Category.category_id == Product.category_id)
                .join(SalesDetail, Product.product_id == SalesDetail.product_id)
                .join(SalesInvoice, SalesDetail.invoice_id == SalesInvoice.invoice_id)
                .filter(
                    SalesInvoice.invoice_date >= start_date,
                    SalesInvoice.invoice_date <= end_date,
                )
                .group_by(Category.category_id, Category.category_name)
                .order_by(func.sum(SalesDetail.unit_price * SalesDetail.quantity).desc())
                .all()
            )
            return [
                (
                    str(row[0]),
                    float(row[1] if row[1] is not None else 0.0),
                )
                for row in results
            ]
        except Exception as e:
            logger.error("Lỗi khi truy vấn doanh thu theo danh mục [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_revenue_by_payment_method(
        self, start_date: datetime, end_date: datetime
    ) -> List[Tuple[str, float, int]]:
        try:
            results = (
                self.session.query(
                    SalesInvoice.payment_method,
                    func.sum(SalesInvoice.final_total),
                    func.count(SalesInvoice.invoice_id),
                )
                .filter(
                    SalesInvoice.invoice_date >= start_date,
                    SalesInvoice.invoice_date <= end_date,
                )
                .group_by(SalesInvoice.payment_method)
                .all()
            )
            return [
                (
                    str(row[0] if row[0] is not None else "Cash"),
                    float(row[1] if row[1] is not None else 0.0),
                    int(row[2] if row[2] is not None else 0),
                )
                for row in results
            ]
        except Exception as e:
            logger.error("Lỗi khi truy vấn doanh thu theo phương thức thanh toán [%s - %s]: %s", start_date, end_date, e)
            raise e


    def get_revenue_by_hour(self, start_date: datetime, end_date: datetime) -> List[Tuple[int, float]]:
        try:
            hour_col = extract("hour", SalesInvoice.invoice_date)
            results = (
                self.session.query(
                    hour_col.label("hour_val"),
                    func.sum(SalesInvoice.final_total).label("rev"),
                )
                .filter(
                    SalesInvoice.invoice_date >= start_date,
                    SalesInvoice.invoice_date <= end_date,
                )
                .group_by(hour_col)
                .order_by(hour_col.asc())
                .all()
            )
            return [
                (
                    int(row[0] if row[0] is not None else 0),
                    float(row[1] if row[1] is not None else 0.0),
                )
                for row in results
            ]
        except Exception as e:
            logger.error("Lỗi khi truy vấn doanh thu theo giờ [%s - %s]: %s", start_date, end_date, e)
            raise e
