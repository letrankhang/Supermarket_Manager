import logging
import random
from typing import Optional
from config.database import Database
from src.entities.user import User
from src.services.ForgotpasswordService import ForgotpasswordService
from src.repositories.impl.ForgotpasswordRepositoryImpl import ForgotpasswordRepositoryImpl
from src.utils.EmailHelper import EmailHelper

logger = logging.getLogger(__name__)


class ForgotpasswordServiceImpl(ForgotpasswordService):
    """
    Concrete implementation of ForgotpasswordService with verification code email sending.
    """

    def forgotpassword(self, email: str) -> Optional[User]:
        """
        Retrieves a user by their registered email address and sends a 6-digit verification code.
        """
        try:
            logger.info("Service: Đang tìm kiếm tài khoản với email: %s", email)
            with Database.get_session_ctx() as db_session:
                repo = ForgotpasswordRepositoryImpl(db_session)
                user = repo.find_by_email(email)
                
                if not user:
                    logger.warning("Không tìm thấy tài khoản nào khớp với email: %s", email)
                    return None

                # Phát sinh mã xác thực 6 số ngẫu nhiên
                code = f"{random.randint(100000, 999999)}"
                logger.info("Đã phát sinh mã xác thực: %s cho email: %s", code, email)
                
                # Lưu mã xác thực tạm thời vào bộ nhớ
                from src.services.impl.Verification_codeServiceImpl import VerificationCodeServiceImpl
                VerificationCodeServiceImpl.store_code(email, code)
                
                # Gửi email chứa mã xác thực
                email_sent = EmailHelper.send_verification_code(email, code)
                if not email_sent:
                    logger.error("Gửi email xác thực thất bại tới %s", email)
                    raise Exception("Gửi mã xác thực qua email thất bại. Vui lòng liên hệ quản trị viên hoặc kiểm tra lại cấu hình .env.")

                logger.info("Tìm thấy tài khoản và đã gửi mã xác thực thành công tới email: %s", email)
                return user
        except Exception as e:
            logger.error("Lỗi xảy ra khi xử lý quên mật khẩu cho email %s: %s", email, e)
            raise e