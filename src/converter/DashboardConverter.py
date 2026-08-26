import logging
from datetime import datetime, time, timedelta
from typing import List
from src.entities.sales_invoice import SalesInvoice
from src.dtos.DashboardDTO import RecentTransactionDTO, DashboardDTO
from src.converter.POSConverter import PAYMENT_METHOD_MAP

logger = logging.getLogger(__name__)

PAYMENT_METHOD_LABELS = {code: label for label, code in PAYMENT_METHOD_MAP.items()}

class DashboardConverter:
    @staticmethod
    def format_invoice_time(invoice_date: datetime) -> str:
        if not invoice_date:
            return ""
            
        try:
            now = datetime.now()
            today_start = datetime.combine(now.date(), time.min)
            yesterday_start = today_start - timedelta(days=1)

            if invoice_date >= today_start:
                # E.g. "10:45 AM"
                return invoice_date.strftime("%I:%M %p")
            elif invoice_date >= yesterday_start:
                return "Hôm qua"
            else:
                # E.g. "16/08/2026"
                return invoice_date.strftime("%d/%m/%Y")
        except Exception as e:
            logger.error("Lỗi khi định dạng thời gian hóa đơn: %s", e)
            return invoice_date.strftime("%d/%m/%Y")


    @classmethod
    def to_recent_transaction_dto(cls, invoice: SalesInvoice) -> RecentTransactionDTO:
        invoice_id = invoice.invoice_id
        invoice_code = f"#INV-{invoice_id:03d}"
        formatted_time = cls.format_invoice_time(invoice.invoice_date)
        final_total = float(invoice.final_total) if invoice.final_total is not None else 0.0
        payment_method = PAYMENT_METHOD_LABELS.get(invoice.payment_method, "Tiền mặt")

        return RecentTransactionDTO(
            invoice_id=invoice_id,
            invoice_code=invoice_code,
            invoice_date=invoice.invoice_date,
            formatted_time=formatted_time,
            final_total=final_total,
            payment_method=payment_method
        )


    @classmethod
    def to_dashboard_dto(
        cls,
        today_revenue: float,
        revenue_growth_rate: float,
        today_invoice_count: int,
        invoice_growth_rate: float,
        low_stock_count: int,
        new_customer_count: int,
        customer_growth_rate: float,
        weekly_revenue: List[float],
        recent_invoices: List[SalesInvoice]
    ) -> DashboardDTO:
        recent_tx_dtos = [cls.to_recent_transaction_dto(inv) for inv in recent_invoices]
        
        return DashboardDTO(
            today_revenue=today_revenue,
            revenue_growth_rate=revenue_growth_rate,
            today_invoice_count=today_invoice_count,
            invoice_growth_rate=invoice_growth_rate,
            low_stock_count=low_stock_count,
            new_customer_count=new_customer_count,
            customer_growth_rate=customer_growth_rate,
            weekly_revenue=weekly_revenue,
            recent_transactions=recent_tx_dtos
        )
