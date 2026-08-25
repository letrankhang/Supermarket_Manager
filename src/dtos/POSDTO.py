from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

@dataclass
class CategoryDTO:
    category_id: Optional[int]
    category_name: str

@dataclass
class ProductDTO:
    product_id: int
    barcode: str
    product_name: str
    unit: str
    retail_price: Decimal
    current_stock: int
    image_path: Optional[str] = None
    cost_price: Decimal = Decimal("0")

    @property
    def is_out_of_stock(self) -> bool:
        return self.current_stock <= 0

@dataclass
class CartItemDTO:
    product_id: int
    product_name: str
    unit_price: Decimal
    quantity: int
    stock_available: int
    cost_price: Decimal = Decimal("0")

    @property
    def line_total(self) -> Decimal:
        return self.unit_price * self.quantity

@dataclass
class CartSummaryDTO:
    item_count: int
    sub_total: Decimal
    discount_rate: Decimal
    discount_amount: Decimal
    tax_rate: Decimal
    tax_amount: Decimal
    grand_total: Decimal

@dataclass
class CartDTO:
    items: List[CartItemDTO] = field(default_factory=list)
    summary: Optional[CartSummaryDTO] = None

    @property
    def is_empty(self) -> bool:
        return not self.items

@dataclass
class CheckoutRequestDTO:
    user_id: int
    payment_method_label: str
    customer_id: Optional[int] = None

@dataclass
class CheckoutResultDTO:
    success: bool
    message: str
    invoice_id: Optional[int] = None
    invoice_code: Optional[str] = None
    final_total: Decimal = Decimal("0")
    invoice_date: Optional[datetime] = None

@dataclass
class InvoiceLineDTO:
    """Một dòng sản phẩm trên hóa đơn đã lưu."""
    product_id: int
    product_name: str
    unit: str
    quantity: int
    unit_price: Decimal

    @property
    def line_total(self) -> Decimal:
        return self.unit_price * self.quantity

@dataclass
class InvoiceDetailDTO:
    """Toàn bộ dữ liệu một hóa đơn, dùng để in ra PDF."""
    invoice_id: int
    invoice_code: str
    invoice_date: Optional[datetime]
    cashier_name: str
    customer_name: str
    payment_method: str
    payment_method_label: str
    sub_total: Decimal
    discount_amount: Decimal
    tax_amount: Decimal
    final_total: Decimal
    points_used: int = 0
    lines: List[InvoiceLineDTO] = field(default_factory=list)

    @property
    def item_count(self) -> int:
        return sum(line.quantity for line in self.lines)
