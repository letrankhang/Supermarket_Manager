import sys
import logging
from PyQt6.QtWidgets import QApplication
from config.database import Database
from src.controller.LoginController import LoginController

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger(__name__)

# Configure stdout to use UTF-8 to prevent encoding errors on Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        import sys, codecs
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def main():
    logger.info("=== Khởi tạo Cơ sở Dữ liệu Siêu thị ===")
    try:
        Database.initialize()
        logger.info("Khởi tạo cơ sở dữ liệu thành công.")
    except Exception as e:
        logger.critical("Không thể kết nối hoặc khởi tạo cơ sở dữ liệu: %s", e)
        sys.exit(1)

    # Khởi chạy giao diện PyQt6
    logger.info("Khởi động ứng dụng giao diện...")
    app = QApplication(sys.argv)
    login_window = LoginController()
    login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
