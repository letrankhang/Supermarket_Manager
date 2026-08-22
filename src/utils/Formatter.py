import logging
from decimal import Decimal, InvalidOperation
from typing import Union

from config.settings import POSSettings

logger = logging.getLogger(__name__)

Number = Union[int, float, Decimal]

def format_currency(amount: Number, with_suffix: bool = True) -> str:
    try:
        value = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError):
        logger.warning("Không định dạng được số tiền %s, hiển thị 0.", amount)
        value = Decimal("0")

    formatted = f"{value:,.0f}".replace(",", ".")
    if with_suffix:
        return f"{formatted} {POSSettings.CURRENCY_SUFFIX}"
    return formatted

def format_discount(amount: Number) -> str:
    try:
        value = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError):
        value = Decimal("0")

    if value <= 0:
        return format_currency(0)
    return f"- {format_currency(value)}"

def format_rate_as_percent(rate: Number) -> str:
    try:
        percent = Decimal(str(rate)) * Decimal("100")
    except (InvalidOperation, ValueError, TypeError):
        logger.warning("Không định dạng được tỷ lệ %s, hiển thị 0%%.", rate)
        percent = Decimal("0")

    normalized = percent.normalize()
    text = format(normalized, "f")
    return f"{text.replace('.', ',')}%"
