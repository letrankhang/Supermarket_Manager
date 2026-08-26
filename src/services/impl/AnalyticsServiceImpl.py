import calendar
import logging
from datetime import date, datetime, time, timedelta
from typing import Tuple

from sqlalchemy import func

from config.database import Database
from src.converter.AnalyticsConverter import AnalyticsConverter
from src.dtos.AnalyticsDTO import AnalyticsDTO
from src.entities.sales_invoice import SalesInvoice
from src.repositories.impl.AnalyticsRepositoryImpl import AnalyticsRepositoryImpl
from src.services.AnalyticsService import AnalyticsService


logger = logging.getLogger(__name__)

class AnalyticsServiceImpl(AnalyticsService):
    def get_analytics_by_period(self, period_type: str = "week") -> AnalyticsDTO:
        now = datetime.now()
        period_type_clean = (period_type or "week").strip().lower()

        if period_type_clean == "today":
            curr_start = datetime.combine(now.date(), time.min)
            curr_end = datetime.combine(now.date(), time.max)

            prev_date = now.date() - timedelta(days=1)
            prev_start = datetime.combine(prev_date, time.min)
            prev_end = datetime.combine(prev_date, time.max)

            label = f"Hôm nay ({now.strftime('%d/%m/%Y')})"

        elif period_type_clean == "month":
            _, last_day = calendar.monthrange(now.year, now.month)
            curr_start = datetime(now.year, now.month, 1, 0, 0, 0)
            curr_end = datetime(now.year, now.month, last_day, 23, 59, 59)

            if now.month == 1:
                prev_year = now.year - 1
                prev_month = 12
            else:
                prev_year = now.year
                prev_month = now.month - 1

            _, prev_last_day = calendar.monthrange(prev_year, prev_month)
            prev_start = datetime(prev_year, prev_month, 1, 0, 0, 0)
            prev_end = datetime(prev_year, prev_month, prev_last_day, 23, 59, 59)

            label = f"Tháng {now.month}/{now.year}"

        else:  
            start_of_week = now.date() - timedelta(days=now.weekday())
            end_of_week = start_of_week + timedelta(days=6)

            curr_start = datetime.combine(start_of_week, time.min)
            curr_end = datetime.combine(end_of_week, time.max)

            prev_start_of_week = start_of_week - timedelta(days=7)
            prev_end_of_week = end_of_week - timedelta(days=7)

            prev_start = datetime.combine(prev_start_of_week, time.min)
            prev_end = datetime.combine(prev_end_of_week, time.max)

            label = f"Tuần {now.isocalendar()[1]} ({start_of_week.strftime('%d/%m')} - {end_of_week.strftime('%d/%m/%Y')})"

        return self._fetch_and_calculate_analytics(
            curr_start=curr_start,
            curr_end=curr_end,
            prev_start=prev_start,
            prev_end=prev_end,
            period_label=label,
        )


    def get_analytics_data(self, year: int, month: int) -> AnalyticsDTO:
        try:
            _, last_day = calendar.monthrange(year, month)
            curr_start = datetime(year, month, 1, 0, 0, 0)
            curr_end = datetime(year, month, last_day, 23, 59, 59)

            if month == 1:
                prev_year = year - 1
                prev_month = 12
            else:
                prev_year = year
                prev_month = month - 1

            _, prev_last_day = calendar.monthrange(prev_year, prev_month)
            prev_start = datetime(prev_year, prev_month, 1, 0, 0, 0)
            prev_end = datetime(prev_year, prev_month, prev_last_day, 23, 59, 59)

            label = f"Tháng {month}/{year}"

            return self._fetch_and_calculate_analytics(
                curr_start=curr_start,
                curr_end=curr_end,
                prev_start=prev_start,
                prev_end=prev_end,
                period_label=label,
            )
        except Exception as e:
            logger.error("Lỗi khi lấy dữ liệu analytics theo tháng %s/%s: %s", month, year, e)
            raise e


    def _fetch_and_calculate_analytics(
        self,
        curr_start: datetime,
        curr_end: datetime,
        prev_start: datetime,
        prev_end: datetime,
        period_label: str,
    ) -> AnalyticsDTO:
        try:
            with Database.get_session_ctx() as session:
                repo = AnalyticsRepositoryImpl(session)

                curr_revenue = repo.get_total_revenue(curr_start, curr_end)
                prev_revenue = repo.get_total_revenue(prev_start, prev_end)
                if prev_revenue > 0:
                    revenue_growth = round(((curr_revenue - prev_revenue) / prev_revenue) * 100.0, 1)
                else:
                    revenue_growth = 100.0 if curr_revenue > 0 else 0.0

                curr_invoices = repo.get_invoice_count(curr_start, curr_end)
                prev_invoices = repo.get_invoice_count(prev_start, prev_end)
                if prev_invoices > 0:
                    invoices_growth = round(((curr_invoices - prev_invoices) / prev_invoices) * 100.0, 1)
                else:
                    invoices_growth = 100.0 if curr_invoices > 0 else 0.0

                curr_aov = (curr_revenue / curr_invoices) if curr_invoices > 0 else 0.0
                prev_aov = (prev_revenue / prev_invoices) if prev_invoices > 0 else 0.0
                if prev_aov > 0:
                    aov_growth = round(((curr_aov - prev_aov) / prev_aov) * 100.0, 1)
                else:
                    aov_growth = 0.0

                total_profit = repo.get_total_profit(curr_start, curr_end)

                returning_rate, returning_growth = self._calculate_returning_rate(
                    session=session,
                    curr_start=curr_start,
                    curr_end=curr_end,
                    prev_start=prev_start,
                    prev_end=prev_end,
                )

                daily_rows = repo.get_daily_revenue(curr_start, curr_end)
                top_rows = repo.get_top_products(curr_start, curr_end, limit=5)
                category_rows = repo.get_category_sales(curr_start, curr_end)
                payment_rows = repo.get_revenue_by_payment_method(curr_start, curr_end)
                hour_rows = repo.get_revenue_by_hour(curr_start, curr_end)

                dto = AnalyticsConverter.to_analytics_dto(
                    period_label=period_label,
                    total_revenue=curr_revenue,
                    revenue_growth=revenue_growth,
                    total_invoices=curr_invoices,
                    invoices_growth=invoices_growth,
                    avg_order=curr_aov,
                    aov_growth=aov_growth,
                    returning_rate=returning_rate,
                    returning_growth=returning_growth,
                    total_profit=total_profit,
                    daily_rows=daily_rows,
                    top_rows=top_rows,
                    category_rows=category_rows,
                    payment_rows=payment_rows,
                    hour_rows=hour_rows,
                )

            logger.info("Tính toán số liệu Analytics thành công cho '%s'", period_label)
            return dto

        except Exception as e:
            logger.error("Lỗi trong quá trình tính toán Analytics: %s", e)
            raise e


    def _calculate_returning_rate(
        self,
        session,
        curr_start: datetime,
        curr_end: datetime,
        prev_start: datetime,
        prev_end: datetime,
    ) -> Tuple[float, float]:
        try:
            curr_customer_rows = (
                session.query(SalesInvoice.customer_id)
                .filter(
                    SalesInvoice.invoice_date >= curr_start,
                    SalesInvoice.invoice_date <= curr_end,
                    SalesInvoice.customer_id.isnot(None),
                )
                .all()
            )
            curr_customers = set(r[0] for r in curr_customer_rows if r[0] is not None)

            if not curr_customers:
                return 0.0, 0.0

            returning_count = 0
            for cid in curr_customers:
                total_invoices_for_cust = (
                    session.query(func.count(SalesInvoice.invoice_id))
                    .filter(
                        SalesInvoice.customer_id == cid,
                        SalesInvoice.invoice_date <= curr_end,
                    )
                    .scalar()
                    or 0
                )
                if total_invoices_for_cust > 1:
                    returning_count += 1

            returning_rate = round((returning_count / len(curr_customers)) * 100.0, 1)

            prev_customer_rows = (
                session.query(SalesInvoice.customer_id)
                .filter(
                    SalesInvoice.invoice_date >= prev_start,
                    SalesInvoice.invoice_date <= prev_end,
                    SalesInvoice.customer_id.isnot(None),
                )
                .all()
            )
            prev_customers = set(r[0] for r in prev_customer_rows if r[0] is not None)

            if prev_customers:
                prev_returning_count = 0
                for cid in prev_customers:
                    total_invoices_for_cust = (
                        session.query(func.count(SalesInvoice.invoice_id))
                        .filter(
                            SalesInvoice.customer_id == cid,
                            SalesInvoice.invoice_date <= prev_end,
                        )
                        .scalar()
                        or 0
                    )
                    if total_invoices_for_cust > 1:
                        prev_returning_count += 1
                prev_returning_rate = round((prev_returning_count / len(prev_customers)) * 100.0, 1)
                returning_growth = round(returning_rate - prev_returning_rate, 1)
            else:
                returning_growth = round(returning_rate, 1)

            return returning_rate, returning_growth

        except Exception as e:
            logger.warning("Không tính được tỷ lệ khách quay lại: %s", e)
            return 0.0, 0.0
