"""src/utils/FormIcon.py

Tiện ích gắn ảnh và icon cho các form đăng nhập / quên mật khẩu.

Gom về một chỗ để các màn hình dùng chung thay vì mỗi controller chép lại.
Chỉ lo phần ảnh và hành vi; màu sắc vẫn nằm trong file .ui.
"""

import logging
import os
from typing import Optional

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QToolButton

logger = logging.getLogger(__name__)

# Kích thước icon dùng chung cho mọi form
KICH_THUOC_ICON_TRAI = 30   # Icon bên trái ô nhập (person.png / lock.png)
KICH_THUOC_ICON_MAT = 24    # Icon con mắt bên phải ô mật khẩu (view.png / hide.png)
LE_PHAI_ICON = 10


def duong_dan_anh(ten_file: str) -> str:
    """Trả về đường dẫn tuyệt đối của ảnh trong assets/images, chuỗi rỗng nếu không có."""
    thu_muc_hien_tai = os.path.dirname(os.path.abspath(__file__))
    duong_dan = os.path.abspath(
        os.path.join(thu_muc_hien_tai, "..", "..", "assets", "images", ten_file)
    )
    if not os.path.exists(duong_dan):
        logger.error("Không tìm thấy ảnh tại đường dẫn: %s", duong_dan)
        return ""
    return duong_dan.replace("\\", "/")


def tao_icon(ten_file: str, kich_thuoc: int) -> QIcon:
    """Tải ảnh từ assets/images và scale đúng kích thước pixel mong muốn."""
    path = duong_dan_anh(ten_file)
    if not path:
        return QIcon()

    pixmap = QPixmap(path)
    if pixmap.isNull():
        return QIcon()

    scaled = pixmap.scaled(
        kich_thuoc,
        kich_thuoc,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )
    return QIcon(scaled)


def hien_thi_logo(nhan: QLabel, ten_file: str = "logo.png") -> None:
    """Vẽ logo sắc nét, giữ đúng tỉ lệ gốc thay vì kéo giãn theo khung."""
    path = duong_dan_anh(ten_file)
    if not path:
        return

    pixmap = QPixmap(path)
    if pixmap.isNull():
        logger.error("Không đọc được file logo: %s", path)
        return

    nhan.setScaledContents(False)
    nhan.setPixmap(
        pixmap.scaled(
            nhan.width(),
            nhan.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
    )


def them_icon_trai(o_nhap: QLineEdit, *ten_file: str,
                   kich_thuoc: int = KICH_THUOC_ICON_TRAI) -> None:
    """
    Gắn icon vào mép trái ô nhập.

    Args:
        o_nhap: Ô nhập cần gắn icon.
        *ten_file: Các tên file ảnh ưu tiên theo thứ tự, dùng cái đầu tiên đọc được.
        kich_thuoc: Cạnh của icon tính theo pixel.
    """
    for ten in ten_file:
        icon = tao_icon(ten, kich_thuoc)
        if not icon.isNull():
            o_nhap.addAction(icon, QLineEdit.ActionPosition.LeadingPosition)
            return


def them_nut_an_hien(o_nhap: QLineEdit, kich_thuoc: int = KICH_THUOC_ICON_MAT,
                     le_phai: int = LE_PHAI_ICON) -> Optional[QToolButton]:
    """
    Gắn nút con mắt vào bên trong ô mật khẩu để bật/tắt hiển thị nội dung.

    Kiểu dáng của nút do QSS trong file .ui quyết định (rule QToolButton).

    Returns:
        QToolButton đã gắn, hoặc None nếu thiếu ảnh icon.
    """
    icon_view = QIcon(duong_dan_anh("view.png") or duong_dan_anh("eye.png"))
    icon_hide = QIcon(duong_dan_anh("hide.png") or duong_dan_anh("eye_off.png"))

    if icon_view.isNull() or icon_hide.isNull():
        logger.warning("Thiếu icon con mắt (view/hide.png), bỏ qua nút ẩn/hiện mật khẩu.")
        return None

    nut = QToolButton(o_nhap)
    nut.setIconSize(QSize(kich_thuoc, kich_thuoc))
    nut.setFixedSize(kich_thuoc, kich_thuoc)
    nut.setCursor(Qt.CursorShape.PointingHandCursor)
    nut.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def cap_nhat_icon() -> None:
        dang_an = o_nhap.echoMode() == QLineEdit.EchoMode.Password
        nut.setIcon(icon_view if dang_an else icon_hide)
        nut.setToolTip("Hiện mật khẩu" if dang_an else "Ẩn mật khẩu")

    def chuyen_che_do() -> None:
        dang_an = o_nhap.echoMode() == QLineEdit.EchoMode.Password
        o_nhap.setEchoMode(
            QLineEdit.EchoMode.Normal if dang_an else QLineEdit.EchoMode.Password
        )
        cap_nhat_icon()

    nut.clicked.connect(chuyen_che_do)

    # Đặt nút nằm sát mép phải bên trong ô nhập
    bo_cuc = QHBoxLayout(o_nhap)
    bo_cuc.setContentsMargins(0, 0, le_phai, 0)
    bo_cuc.addStretch()
    bo_cuc.addWidget(nut)

    # Chừa chỗ để chữ không chạy xuống dưới icon
    o_nhap.setTextMargins(0, 0, kich_thuoc + le_phai, 0)
    cap_nhat_icon()
    return nut
