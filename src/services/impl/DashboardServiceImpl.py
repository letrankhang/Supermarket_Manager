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

                # 1. Doanh thu hôm nay và hôm qua
                today_revenue = repo.get_revenue_by_range(today_start, today_end)
                yesterday_revenue = repo.get_revenue_by_range(yesterday_start, yesterday_end)

                if yesterday_revenue == 0.0:
                    revenue_growth_rate = 100.0 if today_revenue > 0.0 else 0.0
                else:
                    revenue_growth_rate = round(((today_revenue - yesterday_revenue) / yesterday_revenue) * 100.0, 2)

                # 2. Số hóa đơn hôm nay và hôm qua
                today_invoice_count = repo.get_invoice_count_by_range(today_start, today_end)
                yesterday_invoice_count = repo.get_invoice_count_by_range(yesterday_start, yesterday_end)

                if yesterday_invoice_count == 0:
                    invoice_growth_rate = 100.0 if today_invoice_count > 0 else 0.0
                else:
                    invoice_growth_rate = round(((today_invoice_count - yesterday_invoice_count) / yesterday_invoice_count) * 100.0, 2)

                # 3. Số sản phẩm sắp hết hàng
                low_stock_count = repo.get_low_stock_count(low_stock_threshold)

                # 4. Khách hàng mới hôm nay và hôm qua
                new_customer_count = repo.get_customer_count_by_range(today_start, today_end)
                yesterday_customer_count = repo.get_customer_count_by_range(yesterday_start, yesterday_end)

                if yesterday_customer_count == 0:
                    customer_growth_rate = 100.0 if new_customer_count > 0 else 0.0
                else:
                    customer_growth_rate = round(((new_customer_count - yesterday_customer_count) / yesterday_customer_count) * 100.0, 2)

                # 5. Doanh thu chia theo 4 tuần của tháng hiện tại
                weekly_revenue: List[float] = []
                year = now.year
                month = now.month
                _, last_day = calendar.monthrange(year, month)

                weeks_boundaries = [
                    (datetime(year, month, 1, 0, 0, 0), datetime(year, month, 7, 23, 59, 59)),
                    (datetime(year, month, 8, 0, 0, 0), datetime(year, month, 14, 23, 59, 59)),
                    (datetime(year, month, 15, 0, 0, 0), datetime(year, month, 21, 23, 59, 59)),
                    (datetime(year, month, 22, 0, 0, 0), datetime(year, month, last_day, 23, 59, 59))
                ]

                for w_start, w_end in weeks_boundaries:
                    w_revenue = repo.get_revenue_by_range(w_start, w_end)
                    weekly_revenue.append(w_revenue)

                # 6. Năm hóa đơn gần nhất
                recent_invoices = repo.get_recent_invoices(5)

                # Ánh xạ ngay trong phạm vi session: ra ngoài entity mất kết nối, không lazy-load được
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
            # DTO rỗng để Dashboard vẫn vẽ được khi truy vấn hỏng
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
