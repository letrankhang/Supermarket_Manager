import logging
from config.database import Database
from src.services.NewPasswordService import NewPasswordService
from src.repositories.impl.NewpasswordRepositoryImpl import NewpasswordRepositoryImpl

logger = logging.getLogger(__name__)

class NewpasswordServiceImpl(NewPasswordService):
    def new_password(self, email: str, password: str) -> bool:
        try:
            logger.info("Service: Đang cập nhật mật khẩu mới cho email: %s", email)
            with Database.get_session_ctx() as db_session:
                repo = NewpasswordRepositoryImpl(db_session)
                result = repo.update_password(email, password)
                if result:
                    logger.info("Cập nhật mật khẩu thành công cho email: %s", email)
                    return True
                else:
                    logger.warning("Không tìm thấy người dùng với email: %s", email)
                    return False
        except Exception as e:
            logger.error("Lỗi xảy ra khi đặt lại mật khẩu cho email %s: %s", email, e)
            raise e
