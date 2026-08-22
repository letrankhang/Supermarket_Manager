"""Bộ gửi email của hệ thống: gom kỹ thuật SMTP và mẫu thư vào cùng một chỗ."""

import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)

TEN_NGUOI_GUI = "Supermarket Manager"
# Giá trị mẫu trong .env.example, còn nguyên nghĩa là người dùng chưa cấu hình
EMAIL_MAU = "your_email@gmail.com"

# Bảng màu của thư: nền gần như trắng, viền nhạt, điểm nhấn cam đất
MAU_NEN_TRANG = "#f6f5f2"       # Nền ngoài cùng, chỉ hơi ngả so với màu giấy
MAU_NEN_THE = "#ffffff"         # Nền khối nội dung
MAU_VIEN = "#e5e1d8"            # Viền ngoài và đường kẻ ngang
MAU_CHU = "#33302b"             # Chữ chính
MAU_CHU_MO = "#a09a90"          # Chữ phụ, nhãn, chân thư
MAU_NHAN = "#c2703a"            # Cam đất, dùng cho mã xác thực
MAU_NHAN_NEN = "#fdf8f3"        # Nền ô mã, nhạt tới mức gần như không thấy
MAU_NHAN_VIEN = "#e6b58c"       # Viền ô mã

FONT = "-apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"


class EmailHelper:
    @staticmethod
    def send_verification_code(to_email: str, code: str, so_phut_hieu_luc: int = 5) -> bool:
        """Gửi thư chứa mã xác thực đặt lại mật khẩu."""
        # so_phut_hieu_luc do service truyền xuống, để câu chữ trong thư khớp hạn mã thật
        subject = f"Mã xác thực đặt lại mật khẩu: {code}"

        # Dùng bảng thay cho div: nhiều ứng dụng mail (Outlook) dựng bảng ổn định hơn
        html_body = f"""
        <html>
        <body style="margin:0; padding:0; background-color:{MAU_NEN_TRANG};">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
                 style="background-color:{MAU_NEN_TRANG}; padding:36px 12px;">
            <tr>
              <td align="center">
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="560"
                       style="width:100%; max-width:560px; background-color:{MAU_NEN_THE};
                              border:1px solid {MAU_VIEN}; border-radius:10px;">

                  <tr>
                    <td style="padding:30px 40px 22px 40px; border-bottom:1px solid {MAU_VIEN};">
                      <div style="font-family:{FONT}; font-size:11px; letter-spacing:2.5px;
                                  text-transform:uppercase; color:{MAU_CHU_MO};">
                        Hệ thống quản lý siêu thị
                      </div>
                      <div style="font-family:{FONT}; font-size:20px; font-weight:600;
                                  color:{MAU_CHU}; padding-top:8px;">
                        Đặt lại mật khẩu
                      </div>
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:28px 40px 4px 40px; font-family:{FONT}; font-size:15px;
                               line-height:1.65; color:{MAU_CHU};">
                      <p style="margin:0 0 14px 0;">Xin chào,</p>
                      <p style="margin:0;">
                        Chúng tôi nhận được yêu cầu đặt lại mật khẩu cho tài khoản của bạn.
                        Nhập mã xác thực bên dưới để tiếp tục.
                      </p>
                    </td>
                  </tr>

                  <tr>
                    <td align="center" style="padding:26px 40px 6px 40px;">
                      <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                          <td style="background-color:{MAU_NHAN_NEN}; border:1px solid {MAU_NHAN_VIEN};
                                     border-radius:8px; padding:16px 17px 16px 26px;">
                            <span style="font-family:{FONT}; font-size:30px; font-weight:600;
                                         letter-spacing:9px; color:{MAU_NHAN};">
                              {code}
                            </span>
                          </td>
                        </tr>
                      </table>
                      <div style="font-family:{FONT}; font-size:12px; color:{MAU_CHU_MO}; padding-top:12px;">
                        Mã có hiệu lực trong {so_phut_hieu_luc} phút và chỉ dùng được một lần
                      </div>
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:24px 40px 30px 40px; font-family:{FONT}; font-size:13px;
                               line-height:1.65; color:{MAU_CHU_MO};">
                      <p style="margin:0;">
                        Vui lòng không chia sẻ mã này cho bất kỳ ai. Nếu bạn không gửi yêu cầu này,
                        hãy bỏ qua thư hoặc liên hệ quản trị viên để đảm bảo an toàn tài khoản.
                      </p>
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:16px 40px 22px 40px; border-top:1px solid {MAU_VIEN};
                               font-family:{FONT}; font-size:11px; color:{MAU_CHU_MO};">
                      Thư tự động, vui lòng không trả lời.
                    </td>
                  </tr>

                </table>
              </td>
            </tr>
          </table>
        </body>
        </html>
        """

        return EmailHelper.send(to_email, subject, html_body)

    @staticmethod
    def send(to_email: str, subject: str, html_body: str) -> bool:
        """Gửi một email HTML. Trả về True nếu gửi được, False nếu thất bại."""
        smtp_host = os.getenv("EMAIL_HOST", "smtp.gmail.com")
        try:
            smtp_port = int(os.getenv("EMAIL_PORT", "587"))
        except ValueError:
            logger.warning("EMAIL_PORT trong .env không phải số, tạm dùng cổng 587.")
            smtp_port = 587

        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not sender_password or sender_email == EMAIL_MAU:
            logger.error(
                "Chưa cấu hình EMAIL_USER/EMAIL_PASSWORD trong file .env. "
                "Với Gmail phải dùng App password 16 ký tự, không dùng mật khẩu tài khoản."
            )
            return False

        msg = MIMEMultipart()
        msg["From"] = f"{TEN_NGUOI_GUI} <{sender_email}>"
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(html_body, "html", "utf-8"))

        try:
            with smtplib.SMTP(smtp_host, smtp_port, timeout=20) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
        except smtplib.SMTPAuthenticationError:
            # Tách riêng vì đây là lỗi hay gặp nhất: dán nhầm mật khẩu tài khoản
            logger.exception(
                "SMTP từ chối đăng nhập tài khoản %s. Kiểm tra lại App password trong .env.",
                sender_email,
            )
            return False
        except Exception:
            logger.exception("Lỗi khi gửi email tới %s qua %s:%s", to_email, smtp_host, smtp_port)
            return False

        logger.info("Đã gửi email tới %s thành công.", to_email)
        return True
