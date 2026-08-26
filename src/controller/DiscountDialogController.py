from typing import Optional
from PySide6.QtWidgets import QDialog, QWidget

from src.gui.discount_dialog_ui import Ui_DiscountDialog

class DiscountDialogController(QDialog, Ui_DiscountDialog):
    def __init__(self, parent: Optional[QWidget] = None, current_discount: float = 0.0) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.spnDiscount.setValue(current_discount)

        self.btnApply.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)


    def get_discount_value(self) -> float:
        return self.spnDiscount.value()