from src.gui.login import Ui_MainWindow


class LoginController(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)