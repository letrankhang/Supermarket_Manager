import sys
import logging
from PyQt6.QtWidgets import QApplication
from config.database import Database
from src.controller.LoginController import LoginController
from src.utils.Theme import apply_light_theme

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger(__name__)

# Console Windows mặc định cp1252, không in nổi tiếng Việt trong log
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

def main():
    logger.info("--- Khởi tạo Cơ sở dữ liệu ---")
    try:
        Database.initialize()
        logger.info("Khởi tạo cơ sở dữ liệu thành công.")
    except Exception as e:
        logger.critical("Không thể kết nối hoặc khởi tạo cơ sở dữ liệu: %s", e)
        sys.exit(1)

    logger.info("Khởi động ứng dụng giao diện...")
    app = QApplication(sys.argv)

    apply_light_theme(app)

    login_window = LoginController()
    login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()