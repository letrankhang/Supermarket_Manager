import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)

SENDER_NAME = "Supermarket Manager"

COLOR_BG_PAGE = "#f6f5f2"       
COLOR_BG_CARD = "#ffffff"        
COLOR_BORDER = "#e5e1d8"            
COLOR_TEXT_PRIMARY = "#33302b"            
COLOR_TEXT_MUTED = "#a09a90"          
COLOR_ACCENT = "#c2703a"           
COLOR_ACCENT_BG = "#fdf8f3"        
COLOR_ACCENT_BORDER = "#e6b58c"     

FONT = "-apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"

class EmailHelper:
    @staticmethod
    def send_verification_code(to_email: str, code: str, valid_minutes: int = 5) -> bool:
        subject = f"Mã xác thực đặt lại mật khẩu: {code}"

        html_body = f"""
        <html>
        <body style="margin:0; padding:0; background-color:{COLOR_BG_PAGE};">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
                 style="background-color:{COLOR_BG_PAGE}; padding:36px 12px;">
            <tr>
              <td align="center">
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="560"
                       style="width:100%; max-width:560px; background-color:{COLOR_BG_CARD};
                              border:1px solid {COLOR_BORDER}; border-radius:10px;">

                  <tr>
                    <td style="padding:30px 40px 22px 40px; border-bottom:1px solid {COLOR_BORDER};">
                      <div style="font-family:{FONT}; font-size:11px; letter-spacing:2.5px;
                                  text-transform:uppercase; color:{COLOR_TEXT_MUTED};">
                        Hệ thống quản lý siêu thị
                      </div>
                      <div style="font-family:{FONT}; font-size:20px; font-weight:600;
                                  color:{COLOR_TEXT_PRIMARY}; padding-top:8px;">
                        Đặt lại mật khẩu
                      </div>
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:28px 40px 4px 40px; font-family:{FONT}; font-size:15px;
                               line-height:1.65; color:{COLOR_TEXT_PRIMARY};">
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
                          <td style="background-color:{COLOR_ACCENT_BG}; border:1px solid {COLOR_ACCENT_BORDER};
                                     border-radius:8px; padding:16px 17px 16px 26px;">
                            <span style="font-family:{FONT}; font-size:30px; font-weight:600;
                                         letter-spacing:9px; color:{COLOR_ACCENT};">
                              {code}
                            </span>
                          </td>
                        </tr>
                      </table>
                      <div style="font-family:{FONT}; font-size:12px; color:{COLOR_TEXT_MUTED}; padding-top:12px;">
                        Mã có hiệu lực trong {valid_minutes} phút và chỉ dùng được một lần
                      </div>
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:24px 40px 30px 40px; font-family:{FONT}; font-size:13px;
                               line-height:1.65; color:{COLOR_TEXT_MUTED};">
                      <p style="margin:0;">
                        Vui lòng không chia sẻ mã này cho bất kỳ ai. Nếu bạn không gửi yêu cầu này,
                        hãy bỏ qua thư hoặc liên hệ quản trị viên để đảm bảo an toàn tài khoản.
                      </p>
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:16px 40px 22px 40px; border-top:1px solid {COLOR_BORDER};
                               font-family:{FONT}; font-size:11px; color:{COLOR_TEXT_MUTED};">
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
        smtp_host = os.getenv("EMAIL_HOST", "smtp.gmail.com")
        try:
            smtp_port = int(os.getenv("EMAIL_PORT", "587"))
        except ValueError:
            logger.warning("EMAIL_PORT trong .env không phải số, tạm dùng cổng 587.")
            smtp_port = 587

        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not sender_password:
            logger.error(
                "Chưa cấu hình EMAIL_USER/EMAIL_PASSWORD trong file .env. "
                "Với Gmail phải dùng App password 16 ký tự, không dùng mật khẩu tài khoản."
            )
            return False

        msg = MIMEMultipart()
        msg["From"] = f"{SENDER_NAME} <{sender_email}>"
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(html_body, "html", "utf-8"))

        try:
            with smtplib.SMTP(smtp_host, smtp_port, timeout=20) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
        except smtplib.SMTPAuthenticationError:
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