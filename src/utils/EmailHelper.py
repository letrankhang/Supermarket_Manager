import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)


class EmailHelper:
    @staticmethod
    def send_verification_code(to_email: str, code: str) -> bool:

        smtp_host = os.getenv("EMAIL_HOST", "smtp.gmail.com")
        try:
            smtp_port_str = os.getenv("EMAIL_PORT", "587")
            smtp_port = int(smtp_port_str)
        except ValueError:
            smtp_port = 587

        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not sender_password or sender_email == "your_email@gmail.com":
            logger.error("Cấu hình Email (EMAIL_USER hoặc EMAIL_PASSWORD) chưa được thiết lập chính xác trong file .env")
            return False

        # Create message
        msg = MIMEMultipart()
        msg["From"] = f"Supermarket Manager <{sender_email}>"
        msg["To"] = to_email
        msg["Subject"] = f"Mã xác thực đặt lại mật khẩu của bạn: {code}"

        # Beautiful HTML Template
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333333; margin: 0; padding: 0;">
            <div style="max-width: 600px; margin: 20px auto; padding: 20px; border: 1px solid #dddddd; border-radius: 8px; background-color: #ffffff;">
                <div style="text-align: center; border-bottom: 2px solid #1abc9c; padding-bottom: 10px; margin-bottom: 20px;">
                    <h2 style="color: #2c3e50; margin: 0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">HỆ THỐNG QUẢN LÝ SIÊU THỊ</h2>
                </div>
                <p style="font-size: 16px;">Xin chào,</p>
                <p style="font-size: 16px;">Chúng tôi nhận được yêu cầu đặt lại mật khẩu cho tài khoản của bạn. Vui lòng sử dụng mã xác thực gồm 6 chữ số dưới đây để tiếp tục:</p>
                <div style="text-align: center; margin: 30px 0;">
                    <span style="font-size: 32px; font-weight: bold; letter-spacing: 6px; color: #ffffff; background-color: #1abc9c; padding: 12px 25px; border-radius: 6px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                        {code}
                    </span>
                </div>
                <p style="font-size: 14px; color: #e74c3c; font-weight: bold;">Mã xác thực này có hiệu lực trong vòng 5 phút và chỉ sử dụng được một lần. Vui lòng không chia sẻ mã này cho bất kỳ ai.</p>
                <p style="font-size: 14px;">Nếu bạn không gửi yêu cầu này, vui lòng bỏ qua email này hoặc liên hệ với quản trị viên để đảm bảo an toàn tài khoản.</p>
                <hr style="border: 0; border-top: 1px solid #eeeeee; margin: 25px 0;">
                <p style="font-size: 12px; color: #7f8c8d; text-align: center; margin: 0;">Đây là email tự động từ Hệ thống Quản lý Siêu thị. Vui lòng không trả lời email này.</p>
            </div>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(body, "html", "utf-8"))

        try:
            with smtplib.SMTP(smtp_host, smtp_port) as server:
                server.starttls()  # Secure connection using TLS
                server.login(sender_email, sender_password)
                server.send_message(msg)
                
            logger.info("Đã gửi email chứa mã xác thực tới %s thành công.", to_email)
            return True
        except Exception as e:
            logger.error("Lỗi xảy ra khi gửi email tới %s: %s", to_email, e)
            return False
