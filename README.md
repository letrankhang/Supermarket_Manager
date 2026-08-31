# 🛒 SUPERMARKET MANAGEMENT SYSTEM (Hệ thống Quản lý Siêu thị)

> Ứng dụng Desktop chuyên nghiệp phục vụ quản lý và vận hành siêu thị/cửa hàng bán lẻ toàn diện, được xây dựng trên nền tảng **Python** và **PySide6 (Qt for Python)** theo kiến trúc phân tầng chuẩn (**Layered Architecture / MVC**).

---

## 👥 Danh Sách Thành Viên & Phân Công Nhiệm Vụ

| STT | Thành Viên | Vai Trò & Phân Hệ Phụ Trách | Nhiệm Vụ Chi Tiết |
| :--- | :--- | :--- | :--- |
| **1** | **Lê Trần Khang** | **Trưởng nhóm / Backend & Core Architecture** | - Xây dựng **Dashboard tổng quan** (KPIs, doanh thu, đơn hàng, cảnh báo tồn kho).<br>- Thiết kế cấu hình chung hệ thống (`config/settings.py`, `config/database.py`).<br>- Module **Đăng nhập, Đăng xuất** & **Quên mật khẩu** (gửi mã OTP qua Email).<br>- Kiến trúc **Phân quyền người dùng (Role-Based Access Control - RBAC)** & Quản lý phiên làm việc (`Session`). |
| **2** | **Lê Hồng Gấm** | **Quản lý Nhân sự & Đối tác** | - Module **Quản lý tài khoản nhân viên** (CRUD nhân viên, phân vai trò, đặt lại mật khẩu, trạng thái hoạt động).<br>- Module **Quản lý Nhà cung cấp** (Thông tin nhà cung ứng, địa chỉ, liên hệ, quản lý danh bạ đối tác cung ứng hàng hóa). |
| **3** | **Trần Thái Kiệt** | **POS Bán hàng & UI/UX Design** | - Phân hệ **POS Bán hàng (Point of Sale)**: Quét/chọn sản phẩm, áp dụng chiết khấu, tính thuế VAT, thanh toán tiền mặt/chuyển khoản, xuất hóa đơn in ấn.<br>- Module **Trung tâm trợ giúp (HelpCenter)**: Hướng dẫn sử dụng và hỗ trợ vận hành.<br>- **Thiết kế & tinh chỉnh giao diện người dùng (UI/UX Styling & Theme)**: Chuẩn hóa hệ thống icon (`qtawesome`), bố cục giao diện và trải nghiệm thao tác. |
| **4** | **Đặng Hoàng Quốc Cường** | **Khách hàng & Báo cáo Phân tích** | - Module **Quản lý Khách hàng (Customer Management)**: Lưu trữ hồ sơ, lịch sử mua hàng, phân hạng khách hàng, tìm kiếm và chọn khách hàng tại quầy.<br>- Phân hệ **Thống kê & Phân tích (Analytics & Reporting)**: Biểu đồ trực quan doanh thu theo thời gian, tỷ trọng danh mục, xu hướng kinh doanh. |
| **5** | **Phan Tuấn Kha** | **Quản lý Hàng hóa & Kho vận** | - Module **Quản lý Sản phẩm (Product Management)**: Quản lý danh mục hàng hóa, giá bán, giá vốn, mã barcode, trạng thái kinh doanh.<br>- Phân hệ **Quản lý Nhập hàng (Purchase / Import Orders)**: Tạo phiếu nhập hàng từ nhà cung cấp, kiểm đếm số lượng, tự động cập nhật số lượng tồn kho. |

---

## 🛠️ Công Nghệ & Thư Viện Sử Dụng

- **Ngôn ngữ lập trình**: Python 3.10+
- **Giao diện người dùng (UI/UX)**: 
  - `PySide6` (Qt6 for Python)
  - `qtawesome` (Bộ icon FontAwesome sắc nét cho Qt)
- **Cơ sở dữ liệu & ORM**: 
  - `SQLAlchemy` (ORM & Database Session Management)
  - `mysql-connector-python` (Hỗ trợ MySQL)
  - `pymssql` (Hỗ trợ Microsoft SQL Server)
- **Bảo mật & Tiện ích**:
  - `bcrypt` (Băm mật khẩu an toàn)
  - `python-dotenv` (Quản lý biến môi trường)
  - `smtplib` & `email.mime` (Gửi email mã OTP xác thực đặt lại mật khẩu)
  - `reportlab` & `Pillow` (Xuất hóa đơn bán hàng chuẩn định dạng PDF)

---

## 🏛️ Cấu Trúc Dự Án (Project Structure)

```text
Supermarket_Manager/
├── assets/                    # Hình ảnh, icon, font chữ và tài nguyên giao diện
├── config/                    # Cấu hình hệ thống
│   ├── database.py            # Quản lý kết nối Database (MySQL / SQL Server)
│   └── settings.py            # Đọc và định nghĩa các tham số hệ thống từ .env
├── src/
│   ├── controller/            # Điều khiển logic giao diện và tương tác người dùng
│   ├── converter/             # Chuyển đổi dữ liệu giữa Entity và DTO
│   ├── dtos/                  # Data Transfer Objects (DTO) truyền dữ liệu
│   ├── entities/              # Định nghĩa bảng và quan hệ ORM (Entities)
│   ├── gui/                   # Giao diện Qt (Dialogs, Windows, Tabs)
│   ├── repositories/          # Tầng truy vấn trực tiếp với Cơ sở dữ liệu
│   ├── services/              # Tầng xử lý logic nghiệp vụ (Business Logic)
│   └── utils/                 # Tiện ích: EmailHelper, PasswordHasher, Theme, InvoicePrinter...
├── .env.example               # File cấu hình mẫu
├── requirements.txt           # Danh sách các thư viện phụ thuộc
├── README.md                  # Tài liệu mô tả và hướng dẫn dự án
└── main.py                    # Điểm khởi chạy chính của ứng dụng
```

---

## ⚙️ Hướng Dẫn Cài Đặt & Cấu Hình

### 1. Yêu cầu tiên quyết
- Đã cài đặt **Python 3.10** trở lên ([Tải Python](https://www.python.org/downloads/)).
- Đã cài đặt hệ quản trị cơ sở dữ liệu: **MySQL** (khuyến nghị XAMPP/MySQL Server) hoặc **Microsoft SQL Server**.

### 2. Cài đặt môi trường và thư viện
Mở Terminal / Command Prompt / PowerShell tại thư mục gốc của dự án và thực hiện các lệnh sau:

```bash
# Tạo môi trường ảo (virtual environment)
python -m venv .venv

# Kích hoạt môi trường ảo:
# Trên Windows PowerShell:
.venv\Scripts\Activate.ps1
# Hoặc trên Command Prompt (cmd):
.venv\Scripts\activate.bat

# Cài đặt các thư viện phụ thuộc:
pip install -r requirements.txt
```

---

### 3. Cấu hình biến môi trường (`.env`)

Tạo file `.env` tại thư mục gốc của dự án (sao chép từ `.env.example`):

```bash
cp .env.example .env
```

Nội dung cấu hình trong file `.env`:

```ini
# ==============================================================================
# 1. CẤU HÌNH DATABASE
# ==============================================================================
# Chọn loại DB: 'mysql' hoặc 'mssql'
DB_TYPE=mysql

# Cấu hình MySQL
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=supermarket_db

# Cấu hình SQL Server (nếu dùng MSSQL)
MSSQL_SERVER=localhost
MSSQL_PORT=1433
MSSQL_USER=sa
MSSQL_PASSWORD=your_mssql_password
MSSQL_NAME=supermarket_db

DB_POOL_NAME=supermarket_pool
DB_POOL_SIZE=5

# ==============================================================================
# 2. CẤU HÌNH BÁN HÀNG & KHO
# ==============================================================================
VAT_RATE=0.08
DEFAULT_DISCOUNT_RATE=0.0
MAX_DISCOUNT_RATE=0.5
LOW_STOCK_THRESHOLD=10
PRODUCT_PAGE_SIZE=60

# ==============================================================================
# 3. CẤU HÌNH EMAIL GỬI MÃ XÁC THỰC (SMTP)
# ==============================================================================
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
```

---

### 4. 📧 Hướng Dẫn Cấu Hình Email Gửi Mã Xác Thực (Google App Password)

Để hệ thống có thể gửi mã xác thực (OTP 6 số) khi nhân viên/quản lý sử dụng tính năng **Quên mật khẩu**, bạn cần cấu hình tài khoản Gmail với **Mật khẩu ứng dụng (App Password)**:

> ⚠️ **Lưu ý bảo mật quan trọng**: 
> - **Không bao giờ** sử dụng mật khẩu đăng nhập trực tiếp của tài khoản Gmail.
> - **Không đưa file `.env` chứa mật khẩu thật lên Git repository**.

#### Các bước tạo App Password trên Gmail:
1. Truy cập vào trang [Google Account Security](https://myaccount.google.com/security).
2. Tại mục **"Cách bạn đăng nhập vào Google"**, đảm bảo bạn đã bật **Xác minh 2 bước (2-Step Verification)**.
3. Tìm kiếm **"Mật khẩu ứng dụng"** (App Passwords) hoặc truy cập trực tiếp link: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
4. Nhập tên ứng dụng (ví dụ: `Supermarket_Manager`) và nhấn **Tạo (Create)**.
5. Google sẽ cấp một chuỗi gồm **16 ký tự** (dạng `xxxx xxxx xxxx xxxx`).
6. Dán chuỗi 16 ký tự này vào biến `EMAIL_PASSWORD` trong file `.env` (bạn có thể giữ nguyên khoảng trắng hoặc xóa khoảng trắng đều được).
7. Điền địa chỉ Gmail tương ứng vào `EMAIL_USER`.

---

## 🚀 Khởi Chạy Ứng Dụng

Sau khi hoàn tất cấu hình cơ sở dữ liệu và file `.env`, khởi chạy hệ thống bằng lệnh:

```bash
python main.py
```

- Hệ thống sẽ tự động kiểm tra và khởi tạo cấu trúc bảng Database (nếu chưa tồn tại).
- Màn hình đăng nhập sẽ hiển thị, cho phép người dùng đăng nhập theo vai trò được phân quyền.

---

## 🔐 Phân Quyền Hệ Thống (RBAC)

Hệ thống hỗ trợ các nhóm vai trò với quyền hạn tách biệt:
- **Quản trị viên (Admin)**: Toàn quyền truy cập Dashboard, quản lý nhân viên, cấu hình, sản phẩm, nhà cung cấp, khách hàng và xem báo cáo tài chính.
- **Thu ngân (Cashier)**: Sử dụng phân hệ POS bán hàng, tìm kiếm khách hàng, áp dụng chiết khấu trong hạn mức, in hóa đơn.
- **Nhân viên kho (Inventory Staff)**: Quản lý sản phẩm, lập phiếu nhập hàng, theo dõi mức tồn kho và cảnh báo hết hàng.

---

## 📄 Bản Quyền & Giấy Phép

- Dự án được thực hiện trong khuôn khổ **bài tập lớn cuối kì học phần Lập trình Python và ứng dụng**.
- Phục vụ mục đích học tập và nghiên cứu ứng dụng phần mềm quản lý bán lẻ. Mọi đóng góp và mã nguồn tuân thủ các quy định học thuật của nhóm.

