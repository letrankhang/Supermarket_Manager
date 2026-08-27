import logging

from typing import List, Optional
from config.database import Database
from src.converter.CategoryConverter import CategoryConverter
from src.dtos.CategoryDTO import CategoryDTO, CreateCategoryDTO, UpdateCategoryDTO
from src.repositories.CategoryRepository import CategoryRepository
from src.repositories.impl.CategoryRepositoryImpl import CategoryRepositoryImpl

logger = logging.getLogger(__name__)

class CategoryService:

    def __init__(self, repository: Optional[CategoryRepository] = None) -> None:
        self._repo: CategoryRepository = repository or CategoryRepositoryImpl()

    def get_all_categories(self) -> List[CategoryDTO]:
        try:
            with Database.get_session_ctx() as session:
                entities = self._repo.list_all(session)
                return [CategoryConverter.to_dto(e) for e in entities]
        except Exception:
            logger.exception("Lỗi khi lấy danh sách danh mục")
            raise RuntimeError(
                "Không thể tải danh sách danh mục. Vui lòng thử lại sau."
            )

    def create_category(self, dto: CreateCategoryDTO) -> CategoryDTO:
        self._validate_input(dto.category_name)

        try:
            with Database.get_session_ctx() as session:
                existing = self._repo.get_by_name(session, dto.category_name)

                if existing is not None:
                    raise ValueError(
                        f"Danh mục '{dto.category_name}' đã tồn tại."
                    )

                entity = CategoryConverter.to_entity_for_create(dto)
                created = self._repo.create(session, entity)

                return CategoryConverter.to_dto(created)

        except ValueError:
            raise
        except Exception:
            logger.exception("Lỗi khi tạo danh mục mới")
            raise RuntimeError(
                "Không thể tạo danh mục. Vui lòng thử lại sau."
            )

    def update_category(self, dto: UpdateCategoryDTO) -> CategoryDTO:
        self._validate_input(dto.category_name)

        try:
            with Database.get_session_ctx() as session:
                entity = self._repo.get_by_id(session, dto.category_id)

                if entity is None:
                    raise ValueError(
                        "Không tìm thấy danh mục cần cập nhật."
                    )

                existing = self._repo.get_by_name(session, dto.category_name)

                if (
                    existing is not None
                    and existing.category_id != dto.category_id
                ):
                    raise ValueError(
                        f"Danh mục '{dto.category_name}' đã tồn tại."
                    )

                CategoryConverter.apply_update(entity, dto)
                updated = self._repo.update(session, entity)

                return CategoryConverter.to_dto(updated)

        except ValueError:
            raise
        except Exception:
            logger.exception(
                "Lỗi khi cập nhật danh mục có mã ID=%s",
                dto.category_id,
            )
            raise RuntimeError(
                "Không thể cập nhật danh mục. Vui lòng thử lại sau."
            )

    def delete_category(self, category_id: int) -> None:
        try:
            with Database.get_session_ctx() as session:
                deleted = self._repo.delete(session, category_id)

                if not deleted:
                    raise ValueError(
                        "Không tìm thấy danh mục cần xóa."
                    )

        except ValueError:
            raise
        except Exception:
            logger.exception(
                "Lỗi khi xóa danh mục có mã ID=%s",
                category_id,
            )
            raise RuntimeError(
                "Không thể xóa danh mục. "
                "Có thể danh mục này đang được sử dụng bởi một hoặc nhiều sản phẩm."
            )

    @staticmethod
    def _validate_input(category_name: str) -> None:
        if not category_name or not category_name.strip():
            raise ValueError(
                "Tên danh mục không được để trống."
            )