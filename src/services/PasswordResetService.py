from abc import ABC, abstractmethod


class PasswordResetError(Exception):
    """Lỗi nghiệp vụ của luồng đặt lại mật khẩu. Thông điệp đã sẵn sàng hiển thị cho người dùng."""


class InvalidEmailError(PasswordResetError):
    """Email sai định dạng."""


class EmailSendError(PasswordResetError):
    """Không gửi được email chứa mã xác thực."""


class ResendTooSoonError(PasswordResetError):
    """Bấm gửi lại mã quá sớm, còn trong thời gian chờ."""


class InvalidCodeError(PasswordResetError):
    """Mã xác thực không đúng."""


class CodeExpiredError(PasswordResetError):
    """Mã xác thực đã hết hạn hoặc chưa được gửi."""


class TooManyAttemptsError(PasswordResetError):
    """Nhập sai mã quá số lần cho phép, mã đã bị hủy."""


class InvalidResetTokenError(PasswordResetError):
    """Chưa xác thực mã hoặc phiên đặt lại mật khẩu đã hết hạn."""


class WeakPasswordError(PasswordResetError):
    """Mật khẩu mới không đạt yêu cầu tối thiểu."""


class PasswordResetService(ABC):
    """
    Nghiệp vụ quên mật khẩu, gồm 3 bước nối tiếp nhau:
        1. send_code       - gửi mã xác thực tới email
        2. verify_code     - đối chiếu mã, trả về vé đặt lại mật khẩu
        3. reset_password  - đổi mật khẩu, bắt buộc kèm vé ở bước 2

    Ba bước dùng chung một kho mã tạm nên gom vào cùng một service.
    """

    @abstractmethod
    def send_code(self, email: str) -> None:
        """
        Gửi mã xác thực tới email.

        Cố tình KHÔNG báo email có tồn tại hay không để tránh lộ danh sách
        tài khoản đã đăng ký. Email lạ vẫn kết thúc êm, chỉ ghi log nội bộ.
        """

    @abstractmethod
    def verify_code(self, email: str, code: str) -> str:
        """
        Đối chiếu mã xác thực.

        Returns:
            str: Vé đặt lại mật khẩu, phải đưa lại cho reset_password.
        """

    @abstractmethod
    def reset_password(self, email: str, reset_token: str, new_password: str) -> None:
        """Đổi mật khẩu sau khi đã xác thực mã thành công."""
