import logging

from decimal import Decimal, InvalidOperation
from typing import Optional

from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtWidgets import QDialog, QWidget

from src.gui.cash_payment_dialog_ui import Ui_CashPaymentDialog
from src.utils.Formatter import format_currency

logger = logging.getLogger(__name__)

QUICK_AMOUNTS = {
    "btnQuick50": Decimal("50000"),
    "btnQuick100": Decimal("100000"),
    "btnQuick200": Decimal("200000"),
    "btnQuick500": Decimal("500000"),
}

NOT_ENOUGH_MESSAGE = "Số tiền khách đưa không đủ"

class CashPaymentDialogController(QDialog, Ui_CashPaymentDialog):
    def __init__(self, parent: Optional[QWidget] = None, total_amount: Decimal = Decimal("0")) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.total_amount = total_amount
        self.cash_received = Decimal("0")

        self.lblTotalValue.setText(format_currency(self.total_amount))

        self._setup_input()
        self._setup_signals()
        self._update_change()


    def _setup_input(self) -> None:
        expression = QRegularExpression(r"[0-9.]{0,20}")
        self.txtCashReceived.setValidator(
            QRegularExpressionValidator(expression, self)
        )
        self.txtCashReceived.setFocus()


    def _setup_signals(self) -> None:
        self.txtCashReceived.textEdited.connect(self._on_cash_text_edited)
        self.txtCashReceived.returnPressed.connect(self._on_confirm)

        for button_name, amount in QUICK_AMOUNTS.items():
            button = getattr(self, button_name, None)
            if button is None:
                logger.warning("Không tìm thấy nút mệnh giá nhanh '%s'.", button_name)
                continue
            button.clicked.connect(
                lambda checked=False, value=amount: self._on_quick_amount(value)
            )

        self.btnExactAmount.clicked.connect(self._on_exact_amount)
        self.btnConfirm.clicked.connect(self._on_confirm)
        self.btnCancel.clicked.connect(self.reject)


    def _on_cash_text_edited(self, text: str) -> None:
        amount = self._parse_amount(text)
        self._set_amount_text(amount)
        self._update_change()


    def _on_quick_amount(self, amount: Decimal) -> None:
        current = self._parse_amount(self.txtCashReceived.text())
        self._set_amount_text(current + amount)
        self._update_change()


    def _on_exact_amount(self) -> None:
        self._set_amount_text(self.total_amount)
        self._update_change()


    def _set_amount_text(self, amount: Decimal) -> None:
        if amount <= 0:
            self.txtCashReceived.setText("")
            return
        self.txtCashReceived.setText(format_currency(amount, with_suffix=False))


    def _parse_amount(self, text: str) -> Decimal:
        digits = "".join(character for character in (text or "") if character.isdigit())
        if not digits:
            return Decimal("0")
        try:
            return Decimal(digits)
        except InvalidOperation:
            logger.warning("Số tiền khách đưa không hợp lệ: %s", text)
            return Decimal("0")


    def _update_change(self) -> None:
        received = self._parse_amount(self.txtCashReceived.text())
        change = received - self.total_amount

        if change >= 0:
            self.lblChangeValue.setText(format_currency(change))
            self.lblError.setText("")
            self.btnConfirm.setEnabled(True)
        else:
            self.lblChangeValue.setText(format_currency(0))
            if received > 0:
                self.lblError.setText(
                    NOT_ENOUGH_MESSAGE + ", còn thiếu "
                    + format_currency(self.total_amount - received) + "."
                )
            else:
                self.lblError.setText("")
            self.btnConfirm.setEnabled(False)


    def _on_confirm(self) -> None:
        received = self._parse_amount(self.txtCashReceived.text())

        if received < self.total_amount:
            self.lblError.setText(NOT_ENOUGH_MESSAGE + ".")
            self.btnConfirm.setEnabled(False)
            return

        self.cash_received = received
        self.accept()


    def get_cash_received(self) -> Decimal:
        return self.cash_received


    def get_change_amount(self) -> Decimal:
        change = self.cash_received - self.total_amount
        if change < 0:
            return Decimal("0")
        return change
