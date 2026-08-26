import logging
import calendar
from datetime import datetime, time, timedelta
from typing import List

from config.database import Database
from src.dtos.DashboardDTO import DashboardDTO
from src.converter.DashboardConverter import DashboardConverter
from src.services.DashboardService import DashboardService
from src.repositories.impl.DashboardRepositoryImpl import DashboardRepositoryImpl


logger = logging.getLogger(__name__)

RECENT_TRANSACTION_LIMIT = 20

class DashboardServiceImpl(DashboardService):
    def get_dashboard_data(self, low_stock_threshold: int = 10) -> DashboardDTO:
        try:
            now = datetime.now()
            
            today_start = datetime.combine(now.date(), time.min)
            today_end = datetime.combine(now.date(), time.max)
            
            yesterday_start = today_start - timedelta(days=1)
            yesterday_end = today_end - timedelta(days=1)

            with Database.get_session_ctx() as session:
                repo = DashboardRepositoryImpl(session)

                today_revenue = repo.get_revenue_by_range(today_start, today_end)
                yesterday_revenue = repo.get_revenue_by_range(yesterday_start, yesterday_end)

                if yesterday_revenue == 0.0:
                    revenue_growth_rate = 100.0 if today_revenue > 0.0 else 0.0
                else:
                    revenue_growth_rate = round(((today_revenue - yesterday_revenue) / yesterday_revenue) * 100.0, 2)

                today_invoice_count = repo.get_invoice_count_by_range(today_start, today_end)
                yesterday_invoice_count = repo.get_invoice_count_by_range(yesterday_start, yesterday_end)

                if yesterday_invoice_count == 0:
                    invoice_growth_rate = 100.0 if today_invoice_count > 0 else 0.0
                else:
                    invoice_growth_rate = round(((today_invoice_count - yesterday_invoice_count) / yesterday_invoice_count) * 100.0, 2)

                low_stock_count = repo.get_low_stock_count(low_stock_threshold)

                new_customer_count = repo.get_customer_count_by_range(today_start, today_end)
                yesterday_customer_count = repo.get_customer_count_by_range(yesterday_start, yesterday_end)

                if yesterday_customer_count == 0:
                    customer_growth_rate = 100.0 if new_customer_count > 0 else 0.0
                else:
                    customer_growth_rate = round(((new_customer_count - yesterday_customer_count) / yesterday_customer_count) * 100.0, 2)

                weekly_revenue = self._weekly_revenue(repo, now.year, now.month)

                recent_invoices = repo.get_recent_invoices(RECENT_TRANSACTION_LIMIT)

                dashboard_dto = DashboardConverter.to_dashboard_dto(
                    today_revenue=today_revenue,
                    revenue_growth_rate=revenue_growth_rate,
                    today_invoice_count=today_invoice_count,
                    invoice_growth_rate=invoice_growth_rate,
                    low_stock_count=low_stock_count,
                    new_customer_count=new_customer_count,
                    customer_growth_rate=customer_growth_rate,
                    weekly_revenue=weekly_revenue,
                    recent_invoices=recent_invoices
                )

            logger.info("Dashboard statistics calculated successfully.")
            return dashboard_dto

        except Exception as e:
            logger.error("Lỗi khi lấy dữ liệu tổng hợp Dashboard: %s", e)
            return DashboardDTO(
                today_revenue=0.0,
                revenue_growth_rate=0.0,
                today_invoice_count=0,
                invoice_growth_rate=0.0,
                low_stock_count=0,
                new_customer_count=0,
                customer_growth_rate=0.0,
                weekly_revenue=[0.0, 0.0, 0.0, 0.0],
                recent_transactions=[]
            )


    def _weekly_revenue(self, repo: DashboardRepositoryImpl, year: int, month: int) -> List[float]:
        _, last_day = calendar.monthrange(year, month)

        weeks_boundaries = [
            (datetime(year, month, 1, 0, 0, 0), datetime(year, month, 7, 23, 59, 59)),
            (datetime(year, month, 8, 0, 0, 0), datetime(year, month, 14, 23, 59, 59)),
            (datetime(year, month, 15, 0, 0, 0), datetime(year, month, 21, 23, 59, 59)),
            (datetime(year, month, 22, 0, 0, 0), datetime(year, month, last_day, 23, 59, 59))
        ]

        weekly_revenue: List[float] = []
        for w_start, w_end in weeks_boundaries:
            weekly_revenue.append(repo.get_revenue_by_range(w_start, w_end))

        return weekly_revenue


    def get_weekly_revenue(self, year: int, month: int) -> List[float]:
        try:
            with Database.get_session_ctx() as session:
                repo = DashboardRepositoryImpl(session)
                return self._weekly_revenue(repo, year, month)
        except Exception as e:
            logger.error("Không lấy được doanh thu tuần của tháng %s/%s: %s", month, year, e)
            return [0.0, 0.0, 0.0, 0.0]
