import io
import logging
import os

from decimal import Decimal
from typing import TYPE_CHECKING, List, Optional, Tuple
from xml.sax.saxutils import escape

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from PIL import Image as PILImage
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    )
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    colors = None
    A4 = (595.27, 841.89)
    ParagraphStyle = None
    mm = 2.834645669291339
    pdfmetrics = None
    PILImage = None
    TTFont = None
    Image = Paragraph = SimpleDocTemplate = Spacer = Table = TableStyle = None

if TYPE_CHECKING:
    from reportlab.lib.styles import ParagraphStyle as ParagraphStyleType
    from reportlab.platypus import Image as ImageType, Table as TableType

from src.dtos.POSDTO import InvoiceDetailDTO
from src.utils.Formatter import format_currency


logger = logging.getLogger(__name__)

STORE_NAME = "SIÊU THỊ RETAILPRO ERP"
STORE_ADDRESS = "Hệ thống quản lý bán hàng"

PAGE_SIZE = A4
PAGE_MARGIN_X = 18 * mm
PAGE_MARGIN_TOP = 16 * mm
PAGE_MARGIN_BOTTOM = 16 * mm
CONTENT_WIDTH = PAGE_SIZE[0] - (PAGE_MARGIN_X * 2)

INFO_COL_RATIOS = [0.15, 0.35, 0.15, 0.35]

PRODUCT_COL_RATIOS = [0.07, 0.41, 0.09, 0.08, 0.175, 0.175]

COL_AMOUNT = 5

SUMMARY_VALUE_RATIO = PRODUCT_COL_RATIOS[COL_AMOUNT]
SUMMARY_LABEL_RATIO = 1.0 - SUMMARY_VALUE_RATIO

COLOR_TEXT = "#111827"
COLOR_TEXT_MUTED = "#6b7280"
COLOR_LINE = "#e5e7eb"
COLOR_LINE_STRONG = "#d1d5db"
COLOR_HEADER_BG = "#f3f4f6"

FONT_REGULAR = "InvoiceFont"
FONT_BOLD = "InvoiceFont-Bold"

PROJECT_FONT_DIR = os.path.join("assets", "fonts")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOGO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "logo3.png")
LOGO_HEIGHT = 16 * mm

LOGO_RENDER_DPI = 300

FONT_CANDIDATES: List[Tuple[str, str]] = [
    (os.path.join(PROJECT_FONT_DIR, "DejaVuSans.ttf"),
     os.path.join(PROJECT_FONT_DIR, "DejaVuSans-Bold.ttf")),
    (os.path.join(PROJECT_FONT_DIR, "Arial.ttf"),
     os.path.join(PROJECT_FONT_DIR, "Arial-Bold.ttf")),
    ("C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/segoeuib.ttf"),
    ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf"),
    ("C:/Windows/Fonts/tahoma.ttf", "C:/Windows/Fonts/tahomabd.ttf"),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
     "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
]
_fonts_registered = False

class InvoicePrintError(Exception):
    pass


def _register_fonts() -> bool:
    global _fonts_registered

    if _fonts_registered:
        return True

    for regular_path, bold_path in FONT_CANDIDATES:
        if not os.path.exists(regular_path):
            continue

        try:
            pdfmetrics.registerFont(TTFont(FONT_REGULAR, regular_path))

            if os.path.exists(bold_path):
                pdfmetrics.registerFont(TTFont(FONT_BOLD, bold_path))
            else:
                pdfmetrics.registerFont(TTFont(FONT_BOLD, regular_path))

            _fonts_registered = True
            logger.info("Hóa đơn PDF dùng font: %s", regular_path)
            return True
        except Exception as e:
            logger.warning("Không nạp được font '%s': %s", regular_path, e)

    logger.error(
        "Không tìm thấy font Unicode nào để in hóa đơn. "
        "Hãy đặt DejaVuSans.ttf vào thư mục %s.", PROJECT_FONT_DIR
    )
    return False


def _column_widths(ratios: list) -> list:
    return [CONTENT_WIDTH * ratio for ratio in ratios]


def _style(name: str, size: int, bold: bool = False, align: int = 0,
           color: str = COLOR_TEXT, space_after: int = 0) -> "ParagraphStyleType":
    if bold:
        font_name = FONT_BOLD
    else:
        font_name = FONT_REGULAR

    return ParagraphStyle(
        name=name,
        fontName=font_name,
        fontSize=size,
        leading=size + 4,
        alignment=align,
        textColor=colors.HexColor(color),
        spaceAfter=space_after
    )


def _build_logo() -> Optional["ImageType"]:
    if not os.path.exists(LOGO_PATH):
        logger.warning("Không tìm thấy logo để in lên hóa đơn: %s", LOGO_PATH)
        return None

    try:
        source = PILImage.open(LOGO_PATH)
        source.load()
        image_width, image_height = source.size

        target_height = int(LOGO_HEIGHT / 72 * LOGO_RENDER_DPI)
        if image_height > target_height:
            target_width = max(1, round(image_width * target_height / image_height))
            source = source.resize((target_width, target_height), PILImage.LANCZOS)

        buffer = io.BytesIO()
        source.save(buffer, format="PNG")
        buffer.seek(0)

        logo = Image(
            buffer,
            width=LOGO_HEIGHT * image_width / image_height,
            height=LOGO_HEIGHT,
        )
        logo.hAlign = "CENTER"
        return logo
    except Exception as e:
        logger.warning("Không nạp được logo '%s': %s", LOGO_PATH, e)
        return None


def _build_header(invoice: InvoiceDetailDTO) -> list:
    elements = []

    logo = _build_logo()
    if logo is not None:
        elements.append(logo)
        elements.append(Spacer(1, 2 * mm))

    elements.append(Paragraph(STORE_NAME, _style("store", 15, bold=True, align=1)))
    elements.append(Paragraph(STORE_ADDRESS, _style("addr", 9, align=1, color=COLOR_TEXT_MUTED)))
    elements.append(Spacer(1, 3 * mm))
    elements.append(Paragraph("HÓA ĐƠN BÁN HÀNG", _style("title", 13, bold=True, align=1)))
    elements.append(Spacer(1, 4 * mm))

    if invoice.invoice_date is not None:
        invoice_date_text = invoice.invoice_date.strftime("%d/%m/%Y %H:%M")
    else:
        invoice_date_text = "-"

    info_rows = [
        ["Mã hóa đơn:", invoice.invoice_code, "Ngày:", invoice_date_text],
        ["Thu ngân:", invoice.cashier_name, "Khách hàng:", invoice.customer_name],
    ]

    info_table = Table(info_rows, colWidths=_column_widths(INFO_COL_RATIOS))
    info_table.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, -1), FONT_REGULAR, 9),
        ("FONT", (0, 0), (0, -1), FONT_BOLD, 9),
        ("FONT", (2, 0), (2, -1), FONT_BOLD, 9),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor(COLOR_TEXT)),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    elements.append(info_table)
    elements.append(Spacer(1, 4 * mm))
    return elements


def _build_product_table(invoice: InvoiceDetailDTO) -> "TableType":
    header = ["STT", "Tên sản phẩm", "ĐVT", "SL", "Đơn giá", "Thành tiền"]
    rows = [header]

    order_number = 1
    for line in invoice.lines:
        rows.append([
            str(order_number),
            Paragraph(escape(line.product_name or ""), _style("cell", 9)),
            line.unit,
            str(line.quantity),
            format_currency(line.unit_price, with_suffix=False),
            format_currency(line.line_total, with_suffix=False),
        ])
        order_number = order_number + 1

    table = Table(
        rows,
        colWidths=_column_widths(PRODUCT_COL_RATIOS),
        repeatRows=1
    )
    table.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, 0), FONT_BOLD, 9),
        ("FONT", (0, 1), (-1, -1), FONT_REGULAR, 9),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(COLOR_HEADER_BG)),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor(COLOR_TEXT)),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (2, 0), (3, -1), "CENTER"),
        ("ALIGN", (4, 0), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEABOVE", (0, 0), (-1, 0), 0.6, colors.HexColor(COLOR_LINE_STRONG)),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, colors.HexColor(COLOR_LINE_STRONG)),
        ("LINEBELOW", (0, 1), (-1, -1), 0.4, colors.HexColor(COLOR_LINE)),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def _build_summary(invoice: InvoiceDetailDTO, cash_received: Optional[Decimal], change_amount: Optional[Decimal]) -> "TableType":
    def make_row(label: str, value: str) -> list:
        return [label, value]

    rows = [
        make_row("Tạm tính:", format_currency(invoice.sub_total)),
    ]

    if invoice.discount_amount > 0:
        rows.append(make_row("Giảm giá:", "- " + format_currency(invoice.discount_amount)))

    rows.append(make_row("Thuế VAT:", format_currency(invoice.tax_amount)))

    total_row_index = len(rows)
    rows.append(make_row("TỔNG THANH TOÁN:", format_currency(invoice.final_total)))

    rows.append(make_row("Phương thức:", invoice.payment_method_label))

    if cash_received is not None:
        rows.append(make_row("Tiền khách đưa:", format_currency(cash_received)))

    if change_amount is not None:
        rows.append(make_row("Tiền thối lại:", format_currency(change_amount)))

    column_widths = _column_widths([SUMMARY_LABEL_RATIO, SUMMARY_VALUE_RATIO])

    table = Table(rows, colWidths=column_widths)
    table.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, -1), FONT_REGULAR, 9),
        ("FONT", (0, total_row_index), (-1, total_row_index), FONT_BOLD, 11),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor(COLOR_TEXT)),
        ("TEXTCOLOR", (0, total_row_index + 1), (0, -1), colors.HexColor(COLOR_TEXT_MUTED)),
        ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("LINEABOVE", (0, 0), (-1, 0), 0.6, colors.HexColor(COLOR_LINE_STRONG)),
        ("LINEABOVE", (0, total_row_index), (-1, total_row_index), 0.8, colors.HexColor(COLOR_LINE_STRONG)),
        ("LINEBELOW", (0, total_row_index), (-1, total_row_index), 0.4, colors.HexColor(COLOR_LINE)),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, total_row_index), (-1, total_row_index), 5),
        ("BOTTOMPADDING", (0, total_row_index), (-1, total_row_index), 5),
    ]))
    return table


def export_invoice_pdf(invoice: InvoiceDetailDTO, file_path: str, cash_received: Optional[Decimal] = None, change_amount: Optional[Decimal] = None) -> str:
    if not REPORTLAB_AVAILABLE:
        raise InvoicePrintError("Thư viện 'reportlab' chưa được cài đặt trong môi trường Python.")

    if invoice is None:
        raise InvoicePrintError("Không có dữ liệu hóa đơn để in.")

    if not _register_fonts():
        raise InvoicePrintError(
            "Không tìm thấy font Unicode để in tiếng Việt có dấu. "
            "Hãy chép DejaVuSans.ttf vào thư mục " + PROJECT_FONT_DIR + "."
        )

    try:
        document = SimpleDocTemplate(
            file_path,
            pagesize=PAGE_SIZE,
            leftMargin=PAGE_MARGIN_X,
            rightMargin=PAGE_MARGIN_X,
            topMargin=PAGE_MARGIN_TOP,
            bottomMargin=PAGE_MARGIN_BOTTOM,
            title="Hoa don " + invoice.invoice_code
        )

        elements = []
        elements.extend(_build_header(invoice))
        elements.append(_build_product_table(invoice))
        elements.append(Spacer(1, 4 * mm))

        summary_table = _build_summary(invoice, cash_received, change_amount)
        elements.append(summary_table)

        elements.append(Spacer(1, 8 * mm))
        elements.append(Paragraph(
            "Cảm ơn quý khách và hẹn gặp lại!",
            _style("thanks", 9, align=1, color=COLOR_TEXT_MUTED)
        ))

        document.build(elements)
        logger.info("Đã xuất hóa đơn %s ra file %s", invoice.invoice_code, file_path)
        return file_path
    except Exception as e:
        logger.error("Lỗi khi xuất hóa đơn %s ra PDF: %s", invoice.invoice_code, e)
        raise InvoicePrintError("Không ghi được file PDF: " + str(e))


def build_default_file_name(invoice: InvoiceDetailDTO) -> str:
    code = (invoice.invoice_code or "").replace("#", "").replace("/", "-")
    if not code:
        code = "hoa-don"
    return "HoaDon-" + code + ".pdf"
