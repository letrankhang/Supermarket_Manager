#!/usr/bin/env python
"""tools/seed_sample_data.py

Nạp dữ liệu mẫu cho màn hình Dashboard.

Sinh dữ liệu phủ đúng 4 thẻ thống kê, biểu đồ doanh thu theo tuần và bảng
giao dịch gần đây:

  - Hóa đơn rải từ ngày 1 của tháng hiện tại tới hôm nay, nên cả 4 cột tuần
    của biểu đồ đều có số liệu.
  - Hôm nay nhiều hóa đơn hơn hôm qua, để tỉ lệ tăng trưởng khác 0.
  - Một số sản phẩm để tồn kho thấp, cho thẻ "Sắp hết hàng" chạy.
  - Khách hàng tạo mới cả hôm nay lẫn hôm qua, cho thẻ "Khách hàng mới" chạy.

Cách dùng:
    python tools/seed_sample_data.py            # chỉ chạy khi bảng còn trống
    python tools/seed_sample_data.py --reset    # xóa dữ liệu mẫu cũ rồi nạp lại

Script KHÔNG đụng tới bảng users và roles.
"""

import argparse
import os
import random
import sys
from datetime import datetime, timedelta
from decimal import Decimal

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.database import Database
from src.entities import (Category, Customer, CustomerTier, Product,
                          SalesDetail, SalesInvoice, User)

# Cố định seed để mỗi lần chạy ra cùng một bộ số, tiện đối chiếu khi test
random.seed(20260822)

# Ngưỡng cảnh báo tồn kho, phải khớp low_stock_threshold trong DashboardController
NGUONG_TON_KHO_THAP = 10

CATEGORIES = [
    ("Đồ uống", "Nước ngọt, nước suối, bia"),
    ("Thực phẩm khô", "Mì, gạo, gia vị"),
    ("Sữa và chế phẩm", "Sữa tươi, sữa chua, phô mai"),
    ("Hóa phẩm", "Bột giặt, nước rửa chén"),
    ("Bánh kẹo", "Bánh quy, kẹo, snack"),
]

# (barcode, tên, chỉ số nhóm hàng, đơn vị, giá bán, tồn kho)
# Bốn dòng cuối để tồn kho <= 10 nhằm kích hoạt thẻ "Sắp hết hàng"
PRODUCTS = [
    ("8934673001015", "Nước suối Aquafina 500ml", 0, "Chai", 5000, 240),
    ("8934673002015", "Coca-Cola lon 330ml", 0, "Lon", 10000, 180),
    ("8934673003015", "Bia Tiger lon 330ml", 0, "Lon", 18000, 96),
    ("8936017360015", "Mì Hảo Hảo tôm chua cay", 1, "Gói", 4500, 500),
    ("8936017361015", "Gạo ST25 túi 5kg", 1, "Túi", 185000, 42),
    ("8936017362015", "Nước mắm Nam Ngư 500ml", 1, "Chai", 32000, 75),
    ("8935001800015", "Sữa tươi Vinamilk 1L", 2, "Hộp", 34000, 60),
    ("8935001801015", "Sữa chua Vinamilk lốc 4", 2, "Lốc", 28000, 35),
    ("8938505970015", "Bột giặt Omo 3kg", 3, "Túi", 145000, 24),
    ("8938505971015", "Nước rửa chén Sunlight 1.5L", 3, "Chai", 52000, 8),
    ("8934804020015", "Bánh Oreo 137g", 4, "Hộp", 22000, 6),
    ("8934804021015", "Snack Oishi 40g", 4, "Gói", 7000, 3),
    ("8934804022015", "Kẹo Alpenliebe 100g", 4, "Gói", 15000, 0),
]

TIERS = [
    ("Đồng", 0, 0),
    ("Bạc", 5_000_000, 3),
    ("Vàng", 20_000_000, 7),
]

CUSTOMER_NAMES = [
    "Nguyễn Văn An", "Trần Thị Bình", "Lê Hoàng Cường", "Phạm Thu Dung",
    "Hoàng Minh Đức", "Vũ Thị Giang", "Đặng Quốc Hùng", "Bùi Thị Lan",
    "Ngô Thanh Mai", "Đỗ Văn Nam", "Lý Thị Oanh", "Trịnh Bá Phong",
]

# Số hóa đơn cố định cho 2 ngày cần so sánh tăng trưởng
SO_HOA_DON_HOM_NAY = 6
SO_HOA_DON_HOM_QUA = 4

# Thứ tự xóa phải tôn trọng khóa ngoại: bảng chi tiết trước, bảng cha sau
BANG_XOA_THEO_THU_TU = [
    (SalesDetail, "sales_details"),
    (SalesInvoice, "sales_invoices"),
    (Customer, "customers"),
    (Product, "products"),
    (Category, "categories"),
    (CustomerTier, "customer_tiers"),
]


def dem_du_lieu(session):
    """Đếm số dòng hiện có của các bảng mà script này quản lý."""
    return {ten: session.query(model).count() for model, ten in BANG_XOA_THEO_THU_TU}


def xoa_du_lieu_cu(session):
    """Xóa dữ liệu mẫu cũ theo đúng thứ tự khóa ngoại."""
    for model, ten in BANG_XOA_THEO_THU_TU:
        so_dong = session.query(model).delete()
        print(f"  - Đã xóa {so_dong} dòng khỏi '{ten}'")
    session.flush()


def tao_danh_muc_va_san_pham(session):
    """Tạo nhóm hàng và sản phẩm, trong đó có vài mã tồn kho thấp."""
    danh_muc = []
    for ten, mo_ta in CATEGORIES:
        c = Category(category_name=ten, description=mo_ta)
        session.add(c)
        danh_muc.append(c)
    session.flush()

    san_pham = []
    for barcode, ten, idx_dm, don_vi, gia_ban, ton_kho in PRODUCTS:
        p = Product(
            barcode=barcode,
            product_name=ten,
            category_id=danh_muc[idx_dm].category_id,
            unit=don_vi,
            retail_price=Decimal(str(gia_ban)),
            current_stock=ton_kho,
            # Giá nhập giả định bằng 72% giá bán
            avg_import_price=Decimal(str(round(gia_ban * 0.72))),
        )
        session.add(p)
        san_pham.append(p)
    session.flush()

    sap_het = sum(1 for p in san_pham if p.current_stock <= NGUONG_TON_KHO_THAP)
    print(f"  - {len(danh_muc)} nhóm hàng, {len(san_pham)} sản phẩm "
          f"(trong đó {sap_het} sản phẩm tồn kho <= {NGUONG_TON_KHO_THAP})")
    return san_pham


def tao_khach_hang(session, hom_nay):
    """Tạo hạng thành viên và khách hàng, đặt created_at thủ công để kiểm soát."""
    for tier_name, min_spent, discount in TIERS:
        session.add(CustomerTier(
            tier_name=tier_name,
            min_spent=Decimal(str(min_spent)),
            discount_percent=discount,
        ))
    session.flush()
    hang = session.query(CustomerTier).order_by(CustomerTier.tier_id).all()

    # 3 khách hôm nay, 2 khách hôm qua, phần còn lại rải về quá khứ
    lich_tao = (
        [hom_nay.replace(hour=9, minute=15)] * 3
        + [(hom_nay - timedelta(days=1)).replace(hour=14, minute=30)] * 2
        + [hom_nay - timedelta(days=n) for n in (5, 9, 14, 21, 40, 65, 90)]
    )

    khach = []
    for i, ngay_tao in enumerate(lich_tao):
        c = Customer(
            phone=f"09{i:08d}",
            full_name=CUSTOMER_NAMES[i % len(CUSTOMER_NAMES)],
            total_points=random.randint(0, 500),
            total_spent=Decimal(str(random.randint(0, 25) * 1_000_000)),
            tier_id=random.choice(hang).tier_id,
            created_at=ngay_tao,
        )
        session.add(c)
        khach.append(c)
    session.flush()

    print(f"  - {len(hang)} hạng thành viên, {len(khach)} khách hàng "
          f"(3 tạo hôm nay, 2 tạo hôm qua)")
    return khach


def tao_mot_hoa_don(session, thoi_diem, san_pham, khach, user_id):
    """Dựng 1 hóa đơn kèm 2-4 dòng chi tiết, final_total tính từ chi tiết."""
    chon = random.sample(san_pham, random.randint(2, 4))

    hoa_don = SalesInvoice(
        customer_id=random.choice(khach).customer_id if random.random() < 0.7 else None,
        user_id=user_id,
        invoice_date=thoi_diem,
        sub_total=Decimal("0"),
        final_total=Decimal("0"),
        payment_method=random.choice(["Cash", "Banking", "E-Wallet"]),
    )
    session.add(hoa_don)
    session.flush()

    tong = Decimal("0")
    for sp in chon:
        so_luong = random.randint(1, 6)
        don_gia = Decimal(str(sp.retail_price))
        tong += don_gia * so_luong
        session.add(SalesDetail(
            invoice_id=hoa_don.invoice_id,
            product_id=sp.product_id,
            quantity=so_luong,
            unit_price=don_gia,
            cost_price=Decimal(str(sp.avg_import_price)),
        ))

    # Chiết khấu 5% cho khoảng 1/4 số hóa đơn, cho giống thực tế
    giam = (tong * Decimal("0.05")).quantize(Decimal("1")) if random.random() < 0.25 else Decimal("0")
    hoa_don.sub_total = tong
    hoa_don.discount_amount = giam
    hoa_don.final_total = tong - giam
    return hoa_don


def tao_hoa_don(session, san_pham, khach, user_id, hom_nay):
    """Rải hóa đơn từ ngày 1 của tháng hiện tại tới hôm nay."""
    so_hoa_don = 0
    for ngay in range(1, hom_nay.day + 1):
        if ngay == hom_nay.day:
            so_luong = SO_HOA_DON_HOM_NAY
        elif ngay == hom_nay.day - 1:
            so_luong = SO_HOA_DON_HOM_QUA
        else:
            so_luong = random.randint(1, 5)

        for _ in range(so_luong):
            thoi_diem = datetime(
                hom_nay.year, hom_nay.month, ngay,
                random.randint(7, 21), random.randint(0, 59), random.randint(0, 59)
            )
            # Hóa đơn của hôm nay không được rơi vào tương lai
            if thoi_diem > hom_nay:
                thoi_diem = hom_nay - timedelta(minutes=random.randint(5, 240))
            tao_mot_hoa_don(session, thoi_diem, san_pham, khach, user_id)
            so_hoa_don += 1

    print(f"  - {so_hoa_don} hóa đơn từ ngày 01 tới ngày "
          f"{hom_nay.day:02d}/{hom_nay.month:02d} "
          f"(hôm nay {SO_HOA_DON_HOM_NAY}, hôm qua {SO_HOA_DON_HOM_QUA})")
    return so_hoa_don


def main():
    parser = argparse.ArgumentParser(description="Nạp dữ liệu mẫu cho Dashboard.")
    parser.add_argument("--reset", action="store_true",
                        help="Xóa dữ liệu mẫu cũ trước khi nạp lại.")
    args = parser.parse_args()

    hom_nay = datetime.now()

    with Database.get_session_ctx() as session:
        hien_co = dem_du_lieu(session)
        tong_hien_co = sum(hien_co.values())

        if tong_hien_co > 0 and not args.reset:
            print("\n[DUNG] Trong DB đã có sẵn dữ liệu ở các bảng sau:")
            for ten, so in hien_co.items():
                if so:
                    print(f"  - {ten}: {so} dòng")
            print("\nChạy lại với cờ --reset nếu muốn xóa và nạp lại:")
            print("    python tools/seed_sample_data.py --reset")
            return 1

        admin = session.query(User).filter_by(username="admin").first()
        if admin is None:
            print("[LOI] Không tìm thấy user 'admin'. "
                  "Chạy main.py một lần để hệ thống tự tạo.")
            return 1

        if args.reset and tong_hien_co > 0:
            print("\n[1/4] Xóa dữ liệu mẫu cũ")
            xoa_du_lieu_cu(session)

        print("\n[2/4] Tạo nhóm hàng và sản phẩm")
        san_pham = tao_danh_muc_va_san_pham(session)

        print("\n[3/4] Tạo hạng thành viên và khách hàng")
        khach = tao_khach_hang(session, hom_nay)

        print("\n[4/4] Tạo hóa đơn bán hàng")
        tao_hoa_don(session, san_pham, khach, admin.user_id, hom_nay)

    print("\nHoàn tất. Mở app vào Dashboard, hoặc bấm 'Tải lại dữ liệu' để xem kết quả.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
