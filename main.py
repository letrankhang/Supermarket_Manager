import sys

# Configure stdout to use UTF-8 to prevent encoding errors on Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        import sys, codecs
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

from config.database import Database

def main():
    print("=== Khởi tạo Cơ sở Dữ liệu Siêu thị ===")
    try:
        Database.initialize()
        print("Khởi tạo cơ sở dữ liệu thành công.")
    except Exception as e:
        print(f"[Lỗi] Không thể kết nối hoặc khởi tạo cơ sở dữ liệu: {e}")

if __name__ == "__main__":
    main()
