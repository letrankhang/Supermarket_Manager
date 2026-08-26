from typing import Tuple, Any, List
from src.dtos.AnalyticsDTO import (
    DailyRevenueDTO, TopProductDTO, RevenueByPaymentDTO,
    RevenueByTimeSlotDTO, CategorySalesDTO, AnalyticsDTO,
)

WEEKDAY_MAP = {
    0: "Thứ 2",
    1: "Thứ 3",
    2: "Thứ 4",
    3: "Thứ 5",
    4: "Thứ 6",
    5: "Thứ 7",
    6: "CN",
}


from datetime import date, datetime

class AnalyticsConverter:
    @staticmethod
    def to_daily_revenue_dto(row: Tuple[Any, float, int]) -> DailyRevenueDTO:
        d = row[0]
        if isinstance(d, str):
            try:
                d = datetime.strptime(d[:10], "%Y-%m-%d").date()
            except Exception:
                pass
        day_label = WEEKDAY_MAP.get(d.weekday(), "") if hasattr(d, "weekday") else ""
        return DailyRevenueDTO(
            date=d,
            revenue=float(row[1] if row[1] is not None else 0.0),
            invoice_count=int(row[2] if row[2] is not None else 0),
            day_label=day_label,
        )

    @staticmethod
    def to_top_product_dto(row: Tuple[int, str, int, float]) -> TopProductDTO:
        return TopProductDTO(
            product_id=int(row[0]),
            product_name=str(row[1]),
            total_quantity=int(row[2] if row[2] is not None else 0),
            total_revenue=float(row[3] if row[3] is not None else 0.0)
        )

    @staticmethod
    def to_category_sales_dto(row: Tuple[str, float], total_sales: float) -> CategorySalesDTO:
        cat_rev = float(row[1] if row[1] is not None else 0.0)
        pct = (cat_rev / total_sales * 100.0) if total_sales > 0 else 0.0
        return CategorySalesDTO(
            category_name=str(row[0]),
            total_revenue=cat_rev,
            percentage=round(pct, 1)
        )

    @staticmethod
    def to_revenue_by_payment_dto(row: Tuple[str, float, int]) -> RevenueByPaymentDTO:
        return RevenueByPaymentDTO(
            payment_method=str(row[0]),
            total_revenue=float(row[1] if row[1] is not None else 0.0),
            invoice_count=int(row[2] if row[2] is not None else 0)
        )

    @staticmethod
    def to_revenue_by_time_slot_dto(row: Tuple[Any, float]) -> RevenueByTimeSlotDTO:
        return RevenueByTimeSlotDTO(
            hour=int(row[0]),
            revenue=float(row[1] if row[1] is not None else 0.0)
        )

    @staticmethod
    def to_analytics_dto(
        period_label: str,
        total_revenue: float,
        revenue_growth: float,
        total_invoices: int,
        invoices_growth: float,
        avg_order: float,
        aov_growth: float,
        returning_rate: float,
        returning_growth: float,
        total_profit: float,
        daily_rows: List[Tuple[Any, float, int]],
        top_rows: List[Tuple[int, str, int, float]],
        category_rows: List[Tuple[str, float]],
        payment_rows: List[Tuple[str, float, int]],
        hour_rows: List[Tuple[Any, float]],
    ) -> AnalyticsDTO:
        total_cat_rev = sum(float(r[1] or 0.0) for r in category_rows)
        cat_dtos = [
            AnalyticsConverter.to_category_sales_dto(r, total_cat_rev)
            for r in category_rows
        ]

        return AnalyticsDTO(
            period_label=period_label,
            total_revenue=total_revenue,
            revenue_growth=revenue_growth,
            total_invoices=total_invoices,
            invoices_growth=invoices_growth,
            avg_order_value=avg_order,
            aov_growth=aov_growth,
            returning_rate=returning_rate,
            returning_growth=returning_growth,
            total_profit=total_profit,
            daily_revenues=[AnalyticsConverter.to_daily_revenue_dto(r) for r in daily_rows],
            top_products=[AnalyticsConverter.to_top_product_dto(r) for r in top_rows],
            categories=cat_dtos,
            revenue_by_payment=[AnalyticsConverter.to_revenue_by_payment_dto(r) for r in payment_rows],
            revenue_by_hour=[AnalyticsConverter.to_revenue_by_time_slot_dto(r) for r in hour_rows],
        )
