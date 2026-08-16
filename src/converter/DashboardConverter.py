# File: D:\Python\Supermarket_Manager\src\converter\DashboardConverter.py

import logging
from datetime import datetime, time, timedelta
from typing import List
from src.entities.sales_invoice import SalesInvoice
from src.dtos.DashboardDTO import RecentTransactionDTO, DashboardDTO

logger = logging.getLogger(__name__)


class DashboardConverter:
    """
    Converter class containing utility methods to map sales entities and
    aggregated metrics into Dashboard DTOs.
    """

    @staticmethod
    def format_invoice_time(invoice_date: datetime) -> str:
        """
        Formats the invoice datetime into a human-friendly string.
        - If today: "10:45 AM"
        - If yesterday: "Hôm qua"
        - Older: "dd/MM/yyyy"

        Args:
            invoice_date (datetime): The datetime of the invoice.

        Returns:
            str: Formatted string representing the time.
        """
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
        """
        Maps a SalesInvoice entity to a RecentTransactionDTO.

        Args:
            invoice (SalesInvoice): The sales invoice database entity.

        Returns:
            RecentTransactionDTO: The mapped data transfer object.
        """
        invoice_id = invoice.invoice_id
        # Format code as #INV-001, #INV-002, etc.
        invoice_code = f"#INV-{invoice_id:03d}"
        formatted_time = cls.format_invoice_time(invoice.invoice_date)
        final_total = float(invoice.final_total) if invoice.final_total is not None else 0.0

        return RecentTransactionDTO(
            invoice_id=invoice_id,
            invoice_code=invoice_code,
            invoice_date=invoice.invoice_date,
            formatted_time=formatted_time,
            final_total=final_total
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
        """
        Constructs a complete DashboardDTO using aggregated metrics and raw recent invoice entities.

        Args:
            today_revenue (float): Total revenue today.
            revenue_growth_rate (float): Revenue growth rate today vs yesterday in %.
            today_invoice_count (int): Total count of invoices today.
            invoice_growth_rate (float): Invoice count growth rate today vs yesterday in %.
            low_stock_count (int): Number of products below low stock threshold.
            new_customer_count (int): Number of new customers registered today.
            customer_growth_rate (float): New customer growth rate today vs yesterday in %.
            weekly_revenue (List[float]): List of monthly weekly revenues.
            recent_invoices (List[SalesInvoice]): List of raw SalesInvoice entities to convert.

        Returns:
            DashboardDTO: The finalized system overview DTO.
        """
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
