import logging
from decimal import Decimal, InvalidOperation
from typing import Callable, List, Optional, Tuple

from PySide6.QtCore import QEvent, QObject, QSize, Qt, QTimer, Signal
from PySide6.QtCore import QUrl
from PySide6.QtGui import (QDesktopServices, QKeySequence, QPixmap,
                           QResizeEvent, QShortcut)
from PySide6.QtWidgets import (
    QButtonGroup, QFrame, QHBoxLayout, QInputDialog, QLabel, QLayout,
    QFileDialog, QMessageBox, QPushButton, QSizePolicy, QVBoxLayout, QWidget
)

import qtawesome as qta

from src.dtos.CustomerDTO import CustomerDTO
from src.dtos.POSDTO import CartDTO, CartItemDTO, CategoryDTO, CheckoutRequestDTO, ProductDTO
from src.gui.tabs.pos_ui import Ui_Form
from src.services.POSService import POSError, ProductNotFoundError
from src.services.impl.POSServiceImpl import POSServiceImpl
from src.utils.Formatter import format_currency, format_discount, format_rate_as_percent
from src.utils.Session import Session

logger = logging.getLogger(__name__)

CARD_WIDTH = 159
CARD_HEIGHT = 236
CARD_SPACING = 16

SEARCH_DEBOUNCE_MS = 300

PAYMENT_ICON_SIZE = QSize(14, 14)
PAYMENT_ICON_COLOR = "#64748b"
PAYMENT_ICON_COLOR_ACTIVE = "#1d4ed8"
PAYMENT_ICON_TEXT_GAP = 1

# Nhãn nút thanh toán tiền mặt. Phải khớp với PAYMENT_METHOD_MAP trong POSConverter.
CASH_PAYMENT_LABEL = "Tiền mặt"

class ProductCard(QFrame):
    add_requested = Signal(int)

    def __init__(self, product: ProductDTO, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.product_id = product.product_id
        self.setObjectName("ProductCard")
        self.setFixedSize(QSize(CARD_WIDTH, CARD_HEIGHT))

        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        layout.addWidget(self._create_thumbnail(product.image_path))

        lbl_name = QLabel(product.product_name, self)
        lbl_name.setObjectName("lblCardName")
        lbl_name.setWordWrap(True)
        lbl_name.setFixedHeight(40)
        layout.addWidget(lbl_name)

        lbl_barcode = QLabel(self._build_stock_caption(product), self)
        lbl_barcode.setObjectName("lblCardBarcode")
        layout.addWidget(lbl_barcode)

        layout.addStretch()
        layout.addLayout(self._create_footer(product))

    def _create_thumbnail(self, image_path: Optional[str]) -> QLabel:
        thumbnail = QLabel(self)
        thumbnail.setObjectName("lblCardThumbnail")
        thumbnail.setFixedHeight(84)
        thumbnail.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap = QPixmap(image_path) if image_path else QPixmap()
        if pixmap.isNull():
            thumbnail.setText("Ảnh sản phẩm")
            return thumbnail

        thumbnail.setPixmap(pixmap.scaled(
            QSize(CARD_WIDTH - 20, 84),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
        return thumbnail

    def _build_stock_caption(self, product: ProductDTO) -> str:
        stock_text = "Hết hàng" if product.is_out_of_stock else f"Còn {product.current_stock}"
        return f"{product.barcode} · {stock_text}"

    def _create_footer(self, product: ProductDTO) -> QHBoxLayout:
        footer = QHBoxLayout()
        footer.setContentsMargins(0, 0, 0, 0)

        lbl_price = QLabel(format_currency(product.retail_price), self)
        lbl_price.setObjectName("lblCardPrice")
        footer.addWidget(lbl_price)
        footer.addStretch()

        self.btn_add = QPushButton("+", self)
        self.btn_add.setObjectName("btnCardAdd")
        self.btn_add.setFixedSize(QSize(30, 30))
        self.btn_add.setCursor(Qt.CursorShape.PointingHandCursor)

        self.btn_add.setEnabled(not product.is_out_of_stock)
        self.btn_add.clicked.connect(lambda: self.add_requested.emit(self.product_id))
        footer.addWidget(self.btn_add)

        return footer

class CartRow(QFrame):
    quantity_change_requested = Signal(int, int)
    remove_requested = Signal(int)

    def __init__(self, item: CartItemDTO, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.product_id = item.product_id
        self.setObjectName("CartRow")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 12, 20, 12)
        layout.setSpacing(6)

        layout.addLayout(self._create_top_row(item))
        layout.addLayout(self._create_bottom_row(item))

    def _create_top_row(self, item: CartItemDTO) -> QHBoxLayout:
        top_row = QHBoxLayout()
        top_row.setContentsMargins(0, 0, 0, 0)

        lbl_name = QLabel(item.product_name, self)
        lbl_name.setObjectName("lblCartItemName")
        top_row.addWidget(lbl_name)
        top_row.addStretch()

        lbl_line_total = QLabel(format_currency(item.line_total), self)
        lbl_line_total.setObjectName("lblCartItemTotal")
        top_row.addWidget(lbl_line_total)

        return top_row

    def _create_bottom_row(self, item: CartItemDTO) -> QHBoxLayout:
        bottom_row = QHBoxLayout()
        bottom_row.setContentsMargins(0, 0, 0, 0)

        lbl_unit_price = QLabel(format_currency(item.unit_price), self)
        lbl_unit_price.setObjectName("lblCartItemUnitPrice")
        bottom_row.addWidget(lbl_unit_price)
        bottom_row.addStretch()

        self.btn_decrease = self._create_small_button("-", "btnCartMinus")
        self.btn_decrease.clicked.connect(
            lambda: self.quantity_change_requested.emit(self.product_id, -1)
        )
        bottom_row.addWidget(self.btn_decrease)

        lbl_quantity = QLabel(str(item.quantity), self)
        lbl_quantity.setObjectName("lblCartItemQuantity")
        lbl_quantity.setFixedWidth(32)
        lbl_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bottom_row.addWidget(lbl_quantity)

        self.btn_increase = self._create_small_button("+", "btnCartPlus")
        self.btn_increase.clicked.connect(
            lambda: self.quantity_change_requested.emit(self.product_id, 1)
        )
        bottom_row.addWidget(self.btn_increase)

        self.btn_remove = self._create_small_button("✕", "btnCartRemove")
        self.btn_remove.setToolTip("Xóa sản phẩm khỏi giỏ hàng")
        self.btn_remove.clicked.connect(lambda: self.remove_requested.emit(self.product_id))
        bottom_row.addWidget(self.btn_remove)

        return bottom_row

    def _create_small_button(self, text: str, object_name: str) -> QPushButton:
        button = QPushButton(text, self)
        button.setObjectName(object_name)
        button.setFixedSize(QSize(28, 28))
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        return button

class POSController(QWidget, Ui_Form):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.pos_service = POSServiceImpl()

        self.product_cards: List[ProductCard] = []
        self.grid_columns: int = 0
        self.selected_category_id: Optional[int] = None
        self.search_keyword: str = ""

        # Khách đang gắn vào hóa đơn. None nghĩa là Khách lẻ.
        self.selected_customer: Optional[CustomerDTO] = None

        self._setup_widget_behaviour()
        self._setup_search_debounce()
        self._setup_category_chips()
        self._setup_payment_methods()
        self._setup_connections()
        self._setup_shortcuts()
        self._show_cashier_name()

        self.load_data()

    def _setup_widget_behaviour(self) -> None:
        for button in (self.btnFilter, self.btnAddCustomer, self.btnClearCart,
                       self.btnEditDiscount, self.btnCheckout):
            button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.lblCustomerBadge.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

    def _setup_search_debounce(self) -> None:
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.setInterval(SEARCH_DEBOUNCE_MS)
        self.search_timer.timeout.connect(self._reload_products)

    def _setup_category_chips(self) -> None:
        self.category_group = QButtonGroup(self)
        self.category_group.setExclusive(True)

        categories: List[CategoryDTO] = self.pos_service.get_categories()
        layout = self.horizontalLayout_categories

        for index, category in enumerate(categories):
            chip = self._create_category_chip(category, is_default=(index == 0))
            self.category_group.addButton(chip)

            layout.insertWidget(layout.count() - 1, chip)

    def _create_category_chip(self, category: CategoryDTO, is_default: bool) -> QPushButton:
        chip = QPushButton(category.category_name, self.frame_categories)
        chip.setObjectName("CategoryChip")
        chip.setCheckable(True)
        chip.setChecked(is_default)
        chip.setCursor(Qt.CursorShape.PointingHandCursor)
        chip.setMinimumHeight(32)

        chip.clicked.connect(
            lambda _checked=False, category_id=category.category_id:
            self._on_category_selected(category_id)
        )
        return chip

    def _setup_payment_methods(self) -> None:
        self.payment_group = QButtonGroup(self)
        self.payment_group.setExclusive(True)

        for button in (self.btnPayCash, self.btnPayCard, self.btnPayTransfer):
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            self.payment_group.addButton(button)

        self._setup_payment_icons()
        self.btnPayCash.setChecked(True)

    def _setup_payment_icons(self) -> None:
        icon_config = {
            self.btnPayCash: ("fa5s.money-bill-wave", PAYMENT_ICON_COLOR, PAYMENT_ICON_COLOR_ACTIVE),
            self.btnPayCard: ("fa5s.credit-card", PAYMENT_ICON_COLOR, PAYMENT_ICON_COLOR_ACTIVE),
            self.btnPayTransfer: ("fa5s.university", PAYMENT_ICON_COLOR, PAYMENT_ICON_COLOR_ACTIVE),
            self.btnClearCart: ("fa5s.trash-alt", "#ef4444", "#dc2626"), # Màu đỏ cho nút Xóa
        }

        self.payment_icon_normal = {}
        self.payment_icon_active = {}

        for button, (icon_name, color_normal, color_active) in icon_config.items():
            try:
                self.payment_icon_normal[button] = qta.icon(icon_name, color=color_normal)
                self.payment_icon_active[button] = qta.icon(icon_name, color=color_active)
            except Exception as e:
                logger.error("Không tải được icon '%s' cho nút: %s", icon_name, e)
                continue

            button.setIconSize(PAYMENT_ICON_SIZE)

            if button.text().strip():
                self._apply_icon_text_gap(button)

            button.installEventFilter(self)
            
            # Đăng ký sự kiện đổi màu khi toggle (nếu là nút chọn)
            if button.isCheckable():
                button.toggled.connect(
                    lambda _checked, target=button: self._update_payment_icon(target, hovered=False)
                )
            self._update_payment_icon(button, hovered=False)

    def _apply_icon_text_gap(self, button: QPushButton) -> None:
        gap = " " * PAYMENT_ICON_TEXT_GAP
        if gap and not button.text().startswith(gap):
            button.setText(gap + button.text())

    def _update_payment_icon(self, button: QPushButton, hovered: bool) -> None:
        if button not in self.payment_icon_normal:
            return

        is_highlighted = hovered or button.isChecked()
        icons = self.payment_icon_active if is_highlighted else self.payment_icon_normal
        button.setIcon(icons[button])

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if source in getattr(self, "payment_icon_normal", {}):
            if event.type() == QEvent.Type.Enter:
                self._update_payment_icon(source, hovered=True)
            elif event.type() == QEvent.Type.Leave:
                self._update_payment_icon(source, hovered=False)

        return super().eventFilter(source, event)

    def _setup_connections(self) -> None:
        self.txtSearch.textChanged.connect(self._on_search_text_changed)
        self.txtSearch.returnPressed.connect(self._on_search_submitted)
        self.btnFilter.clicked.connect(self._on_search_submitted)
        self.btnAddCustomer.clicked.connect(self._on_pick_customer)
        self.btnClearCart.clicked.connect(self._on_clear_cart)
        self.btnEditDiscount.clicked.connect(self._on_edit_discount)
        self.btnCheckout.clicked.connect(self._on_checkout)

    def _setup_shortcuts(self) -> None:
        self.shortcut_help = QShortcut(QKeySequence("F1"), self)
        self.shortcut_help.activated.connect(lambda: self._notify_pending("Trợ giúp"))

        self.shortcut_search = QShortcut(QKeySequence("F2"), self)
        self.shortcut_search.activated.connect(self.txtSearch.setFocus)

        self.shortcut_discount = QShortcut(QKeySequence("F3"), self)
        self.shortcut_discount.activated.connect(self.btnEditDiscount.click)

        self.shortcut_quantity = QShortcut(QKeySequence("F4"), self)
        self.shortcut_quantity.activated.connect(lambda: self._notify_pending("Sửa số lượng"))

        self.shortcut_checkout = QShortcut(QKeySequence("F9"), self)
        self.shortcut_checkout.activated.connect(self.btnCheckout.click)

    def _show_cashier_name(self) -> None:
        cashier = Session.get_username() if Session.is_active() else None
        self.lblCashierName.setText(f"Thu ngân: {cashier or '---'}")

    def load_data(self) -> None:
        self._show_cashier_name()
        self._reload_products()
        self._render_cart(self.pos_service.get_cart())

    def _reload_products(self) -> None:
        products = self.pos_service.get_products(
            category_id=self.selected_category_id,
            keyword=self.search_keyword
        )
        logger.info("POS: nạp %d sản phẩm lên lưới.", len(products))
        self.render_products(products)

    def render_products(self, products: List[ProductDTO]) -> None:
        self._clear_layout(self.gridLayout_products)
        self.product_cards = []

        for product in products:
            card = ProductCard(product=product, parent=self.widget_products)
            card.add_requested.connect(self._on_add_product)
            self.product_cards.append(card)

        self.grid_columns = 0
        self._reflow_product_grid()

    def _reflow_product_grid(self) -> None:
        available_width = self.scrollProducts.viewport().width() - 40
        columns = max(1, available_width // (CARD_WIDTH + CARD_SPACING))
        if columns == self.grid_columns:
            return

        self.gridLayout_products.setColumnStretch(self.grid_columns, 0)
        self.grid_columns = columns
        for index, card in enumerate(self.product_cards):
            self.gridLayout_products.addWidget(card, index // columns, index % columns)

        self.gridLayout_products.setColumnStretch(columns, 1)

    def _render_cart(self, cart: CartDTO) -> None:
        self.render_cart(cart.items)

        summary = cart.summary
        self.render_summary(
            item_count=summary.item_count,
            sub_total_text=format_currency(summary.sub_total),
            discount_text=format_discount(summary.discount_amount),
            tax_rate_text=format_rate_as_percent(summary.tax_rate),
            tax_text=format_currency(summary.tax_amount),
            grand_total_text=format_currency(summary.grand_total)
        )

        self.btnCheckout.setEnabled(not cart.is_empty)

    def render_cart(self, cart_items: List[CartItemDTO]) -> None:
        layout = self.verticalLayout_cart
        for index in reversed(range(layout.count())):
            widget = layout.itemAt(index).widget()
            if isinstance(widget, CartRow):
                widget.setParent(None)

        self.lblCartEmpty.setVisible(not cart_items)

        for position, cart_item in enumerate(cart_items):
            row = CartRow(item=cart_item, parent=self.widget_cart)
            row.quantity_change_requested.connect(self._on_change_quantity)
            row.remove_requested.connect(self._on_remove_item)
            layout.insertWidget(position, row)

    def render_summary(self, item_count: int, sub_total_text: str, discount_text: str,
                       tax_rate_text: str, tax_text: str, grand_total_text: str) -> None:
        self.lblSubTotalCaption.setText(f"Tạm tính ({item_count} sản phẩm)")
        self.lblSubTotal.setText(sub_total_text)
        self.lblDiscount.setText(discount_text)
        self.lblTaxCaption.setText(f"Thuế VAT ({tax_rate_text})")
        self.lblTax.setText(tax_text)
        self.lblGrandTotal.setText(grand_total_text)

    def _clear_layout(self, layout: QLayout) -> None:
        while layout.count():
            widget = layout.takeAt(0).widget()
            if widget is not None:
                widget.setParent(None)

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        if self.product_cards:
            self._reflow_product_grid()

    def _on_search_text_changed(self, keyword: str) -> None:
        self.search_keyword = keyword.strip()
        self.search_timer.start()

    def _on_search_submitted(self) -> None:
        self.search_timer.stop()
        keyword = self.search_keyword

        if not keyword:
            self._reload_products()
            return

        try:
            cart = self.pos_service.add_product_by_barcode(keyword)
        except ProductNotFoundError:
            self._reload_products()
            return
        except POSError as e:
            logger.info("POS: không thêm được sản phẩm theo mã vạch: %s", e)
            self._show_warning(str(e))
            return

        self._render_cart(cart)
        self.txtSearch.clear()

    def _on_category_selected(self, category_id: Optional[int]) -> None:
        self.selected_category_id = category_id
        logger.info("POS: lọc theo danh mục id=%s.", category_id)
        self._reload_products()

    def _on_add_product(self, product_id: int) -> None:
        self._run_cart_action(lambda: self.pos_service.add_product_to_cart(product_id))

    def _on_change_quantity(self, product_id: int, delta: int) -> None:
        self._run_cart_action(lambda: self.pos_service.change_item_quantity(product_id, delta))

    def _on_remove_item(self, product_id: int) -> None:
        self._run_cart_action(lambda: self.pos_service.remove_item_from_cart(product_id))

    def _on_pick_customer(self) -> None:
        """Nút '+KH': mở dialog chọn khách rồi cập nhật nhãn trên hóa đơn.

        Nhập vòng ở đây để tránh hai controller import lẫn nhau lúc nạp module.
        """
        from src.controller.CustomerPickerController import CustomerPickerController

        dialog = CustomerPickerController(self, selected_customer=self.selected_customer)

        # exec() trả về 0 khi bấm Hủy hoặc đóng cửa sổ, khi đó giữ nguyên khách cũ
        if not dialog.exec():
            return

        # dialog.selected_customer là None nếu người dùng bấm "Bỏ chọn"
        self.selected_customer = dialog.selected_customer
        self._update_customer_badge()

    def _update_customer_badge(self) -> None:
        if self.selected_customer:
            self.lblCustomerBadge.setText(f"Khách hàng: {self.selected_customer.ten_hien_thi}")
        else:
            self.lblCustomerBadge.setText("Khách hàng lẻ (Mặc định)")

    def _on_clear_cart(self) -> None:
        answer = QMessageBox.question(
            self,
            "Xóa giỏ hàng",
            "Bạn có chắc muốn xóa toàn bộ sản phẩm trong giỏ hàng?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.reset_order()

    def _on_edit_discount(self) -> None:
        from src.controller.DiscountDialogController import DiscountDialogController

        dialog = DiscountDialogController(self)
        if not dialog.exec():
            return

        percent = dialog.get_discount_value()

        try:
            discount_rate = Decimal(str(percent)) / Decimal("100")
        except InvalidOperation:
            logger.warning("POS: mức giảm giá nhập vào không hợp lệ: %s", percent)
            return

        self._run_cart_action(lambda: self.pos_service.apply_discount_rate(discount_rate))

    def _on_checkout(self) -> None:
        if not Session.is_active():
            self._show_error("Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại.")
            return

        if self.pos_service.get_cart().is_empty:
            self._show_warning("Giỏ hàng đang trống. Vui lòng thêm sản phẩm trước khi thanh toán.")
            return

        total_amount = self.pos_service.get_cart().summary.grand_total
        payment_label = self._get_selected_payment_label()

        # Tiền mặt thì mở hộp thoại nhập tiền để tính tiền thối,
        # các phương thức còn lại giữ nguyên hộp xác nhận cũ.
        if payment_label == CASH_PAYMENT_LABEL:
            cash_result = self._ask_cash_payment(total_amount)
            if cash_result is None:
                return
            cash_received, change_amount = cash_result
        else:
            if not self._confirm_payment(total_amount):
                return
            cash_received = None
            change_amount = None

        request = CheckoutRequestDTO(
            user_id=Session.get_user_id(),
            payment_method_label=payment_label,
            customer_id=(self.selected_customer.customer_id
                         if self.selected_customer else None)
        )

        try:
            result = self.pos_service.checkout(request)
        except POSError as e:
            logger.warning("POS: thanh toán không thành công: %s", e)
            self._show_error(str(e))
            return

        QMessageBox.information(self, "Thanh toán thành công", result.message)

        # Hỏi xuất hóa đơn PDF. Người dùng từ chối hay hủy thì đơn vẫn đã thanh toán.
        self._offer_invoice_pdf(result, cash_received, change_amount)

        self._reload_products()
        self.reset_order()

    def _confirm_payment(self, total_amount: Decimal) -> bool:
        formatted_price = format_currency(total_amount)

        confirm = QMessageBox.question(
            self,
            "Xác nhận thanh toán",
            f"Xác nhận thanh toán đơn hàng với tổng tiền: {formatted_price}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes)

        return confirm == QMessageBox.StandardButton.Yes

    def _ask_cash_payment(self, total_amount: Decimal) -> Optional[Tuple[Decimal, Decimal]]:
        """Mở hộp thoại nhập tiền mặt.

        Trả về (tiền khách đưa, tiền thối) nếu người dùng xác nhận,
        trả về None nếu người dùng hủy để dừng luồng thanh toán.
        Nhập vòng ở đây để tránh hai controller import lẫn nhau lúc nạp module.
        """
        from src.controller.CashPaymentDialogController import CashPaymentDialogController

        dialog = CashPaymentDialogController(self, total_amount)
        if not dialog.exec():
            return None

        return dialog.get_cash_received(), dialog.get_change_amount()

    def _offer_invoice_pdf(self, result, cash_received: Optional[Decimal],
                           change_amount: Optional[Decimal]) -> None:
        """Hỏi và xuất hóa đơn vừa thanh toán ra file PDF."""
        if result.invoice_id is None:
            return

        answer = QMessageBox.question(
            self,
            "Xuất hóa đơn",
            "Bạn có muốn xuất hóa đơn này ra file PDF không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes)

        if answer != QMessageBox.StandardButton.Yes:
            return

        invoice = self.pos_service.get_invoice_detail(result.invoice_id)
        if invoice is None:
            self._show_error("Không lấy được dữ liệu hóa đơn để in.")
            return

        from src.utils.InvoicePrinter import (
            InvoicePrintError, build_default_file_name, export_invoice_pdf
        )

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Lưu hóa đơn PDF",
            build_default_file_name(invoice),
            "File PDF (*.pdf)")

        # Hủy hộp thoại lưu file thì thôi, đơn hàng vẫn đã thanh toán xong.
        if not file_path:
            return

        try:
            export_invoice_pdf(invoice, file_path, cash_received, change_amount)
        except InvoicePrintError as e:
            logger.warning("POS: không xuất được hóa đơn PDF: %s", e)
            self._show_error(str(e))
            return
        except Exception as e:
            logger.exception("POS: lỗi ngoài dự kiến khi xuất hóa đơn PDF: %s", e)
            self._show_error("Đã xảy ra lỗi khi xuất hóa đơn PDF.")
            return

        self._ask_open_invoice_file(file_path)

    def _ask_open_invoice_file(self, file_path: str) -> None:
        answer = QMessageBox.question(
            self,
            "Đã lưu hóa đơn",
            "Đã lưu hóa đơn tại:\n" + file_path
            + "\n\nBạn có muốn mở file ngay không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes)

        if answer != QMessageBox.StandardButton.Yes:
            return

        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    def _get_selected_payment_label(self) -> str:
        selected_button = self.payment_group.checkedButton()
        if selected_button is None:
            return "Tiền mặt"
        return selected_button.text().strip()

    def _run_cart_action(self, action: Callable[[], CartDTO]) -> None:
        try:
            cart = action()
        except POSError as e:
            logger.info("POS: thao tác giỏ hàng bị từ chối: %s", e)
            self._show_warning(str(e))
            return
        except Exception as e:
            logger.exception("POS: lỗi ngoài dự kiến khi thao tác giỏ hàng: %s", e)
            self._show_error("Đã xảy ra lỗi khi cập nhật giỏ hàng. Vui lòng thử lại.")
            return

        self._render_cart(cart)

    def reset_order(self) -> None:
        cart = self.pos_service.clear_cart()
        self._render_cart(cart)
        self.lblOrderCode.setText("Đơn hàng mới")

        # Đơn mới thì gỡ khách của đơn cũ ra
        self.selected_customer = None
        self._update_customer_badge()

        self.btnPayCash.setChecked(True)
        self.txtSearch.clear()
        self.txtSearch.setFocus()

    def _show_warning(self, message: str) -> None:
        QMessageBox.warning(self, "Không thực hiện được", message)

    def _show_error(self, message: str) -> None:
        QMessageBox.critical(self, "Lỗi", message)

    def _notify_pending(self, feature_name: str) -> None:
        QMessageBox.information(
            self,
            "Đang phát triển",
            f"Chức năng '{feature_name}' sẽ được bổ sung ở giai đoạn sau."
        )
