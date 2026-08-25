# File: src/services/CategoryService.py
"""Nghiệp vụ Quản lý Danh mục. Nhận vào/trả ra DTO, không lộ Entity ra ngoài."""
from __future__ import annotations

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
            logger.exception("Loi khi lay danh sach danh muc")
            raise RuntimeError("Khong the tai danh sach danh muc. Vui long thu lai.")

    def get_category_by_id(self, category_id: int) -> Optional[CategoryDTO]:
        try:
            with Database.get_session_ctx() as session:
                entity = self._repo.get_by_id(session, category_id)
                return CategoryConverter.to_dto(entity) if entity else None
        except Exception:
            logger.exception("Loi khi lay danh muc id=%s", category_id)
            raise RuntimeError("Khong the tai thong tin danh muc. Vui long thu lai.")

    def create_category(self, dto: CreateCategoryDTO) -> CategoryDTO:
        self._validate_input(dto.category_name)
        try:
            with Database.get_session_ctx() as session:
                existing = self._repo.get_by_name(session, dto.category_name)
                if existing is not None:
                    raise ValueError(f"Danh muc '{dto.category_name}' da ton tai.")

                entity = CategoryConverter.to_entity_for_create(dto)
                created = self._repo.create(session, entity)
                return CategoryConverter.to_dto(created)
        except ValueError:
            raise
        except Exception:
            logger.exception("Loi khi tao danh muc moi")
            raise RuntimeError("Khong the tao danh muc. Vui long thu lai.")

    def update_category(self, dto: UpdateCategoryDTO) -> CategoryDTO:
        self._validate_input(dto.category_name)
        try:
            with Database.get_session_ctx() as session:
                entity = self._repo.get_by_id(session, dto.category_id)
                if entity is None:
                    raise ValueError("Khong tim thay danh muc can cap nhat.")

                existing = self._repo.get_by_name(session, dto.category_name)
                if existing is not None and existing.category_id != dto.category_id:
                    raise ValueError(f"Danh muc '{dto.category_name}' da ton tai.")

                CategoryConverter.apply_update(entity, dto)
                updated = self._repo.update(session, entity)
                return CategoryConverter.to_dto(updated)
        except ValueError:
            raise
        except Exception:
            logger.exception("Loi khi cap nhat danh muc id=%s", dto.category_id)
            raise RuntimeError("Khong the cap nhat danh muc. Vui long thu lai.")

    def delete_category(self, category_id: int) -> None:
        try:
            with Database.get_session_ctx() as session:
                deleted = self._repo.delete(session, category_id)
                if not deleted:
                    raise ValueError("Khong tim thay danh muc can xoa.")
        except ValueError:
            raise
        except Exception:
            logger.exception("Loi khi xoa danh muc id=%s", category_id)
            raise RuntimeError(
                "Khong the xoa danh muc. Co the danh muc dang duoc san pham su dung."
            )

    @staticmethod
    def _validate_input(category_name: str) -> None:
        if not category_name or not category_name.strip():
            raise ValueError("Ten danh muc khong duoc de trong.")