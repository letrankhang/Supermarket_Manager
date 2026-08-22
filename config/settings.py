import logging
import os
from decimal import Decimal, InvalidOperation

from dotenv import load_dotenv


load_dotenv()

logger = logging.getLogger(__name__)


def _get_decimal(env_key: str, default: str) -> Decimal:
    raw_value = os.getenv(env_key, default)
    try:
        return Decimal(str(raw_value).strip())
    except (InvalidOperation, ValueError):
        logger.warning(
            "Giá trị cấu hình '%s' không hợp lệ ('%s'), dùng mặc định '%s'.",
            env_key, raw_value, default
        )
        return Decimal(default)


def _get_int(env_key: str, default: str) -> int:
    raw_value = os.getenv(env_key, default)
    try:
        return int(str(raw_value).strip())
    except ValueError:
        logger.warning(
            "Giá trị cấu hình '%s' không hợp lệ ('%s'), dùng mặc định '%s'.",
            env_key, raw_value, default
        )
        return int(default)


class POSSettings:
    VAT_RATE: Decimal = _get_decimal("VAT_RATE", "0.08")

    DEFAULT_DISCOUNT_RATE: Decimal = _get_decimal("DEFAULT_DISCOUNT_RATE", "0.0")

    MAX_DISCOUNT_RATE: Decimal = _get_decimal("MAX_DISCOUNT_RATE", "0.5")

    LOW_STOCK_THRESHOLD: int = _get_int("LOW_STOCK_THRESHOLD", "10")

    PRODUCT_PAGE_SIZE: int = _get_int("PRODUCT_PAGE_SIZE", "60")

    CURRENCY_SUFFIX: str = os.getenv("CURRENCY_SUFFIX", "đ")

    ALL_CATEGORY_LABEL: str = os.getenv("ALL_CATEGORY_LABEL", "Tất cả")
