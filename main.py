import sys
import logging
from PySide6.QtWidgets import QApplication

from config.database import Database
from src.controller.LoginController import LoginController
from src.utils.Theme import apply_light_theme

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

def main() -> None:
    logging.info("!!! Khởi tạo Cơ sở dữ liệu !!!")
    try:
        Database.initialize()
        logging.info("Khởi tạo cơ sở dữ liệu thành công.")
    except Exception as e:
        logging.critical("Không thể kết nối hoặc khởi tạo cơ sở dữ liệu: %s", e)
        sys.exit(1)

    logging.info("Khởi động ứng dụng giao diện...")
    app = QApplication(sys.argv)

    apply_light_theme(app)

    login_window = LoginController()
    login_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()