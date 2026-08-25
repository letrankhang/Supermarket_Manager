# File: src/repositories/impl/CategoryRepositoryImpl.py
"""Triển khai CategoryRepository bằng SQLAlchemy ORM (ANSI, chạy được cả MySQL/SQL Server)."""
from __future__ import annotations

import logging
from typing import List, Optional

from sqlalchemy.orm import Session

from src.entities.category import Category
from src.repositories.CategoryRepository import CategoryRepository

logger = logging.getLogger(__name__)


class CategoryRepositoryImpl(CategoryRepository):

    def get_by_id(self, session: Session, category_id: int) -> Optional[Category]:
        try:
            return session.query(Category).filter(Category.category_id == category_id).first()
        except Exception:
            logger.exception("Loi khi lay danh muc theo id=%s", category_id)
            raise

    def get_by_name(self, session: Session, category_name: str) -> Optional[Category]:
        try:
            return (
                session.query(Category)
                .filter(Category.category_name == category_name)
                .first()
            )
        except Exception:
            logger.exception("Loi khi lay danh muc theo ten=%s", category_name)
            raise

    def list_all(self, session: Session) -> List[Category]:
        try:
            return session.query(Category).order_by(Category.category_name.asc()).all()
        except Exception:
            logger.exception("Loi khi lay danh sach danh muc")
            raise

    def create(self, session: Session, category: Category) -> Category:
        try:
            session.add(category)
            session.flush()
            return category
        except Exception:
            logger.exception("Loi khi tao danh muc moi")
            raise

    def update(self, session: Session, category: Category) -> Category:
        try:
            session.flush()
            return category
        except Exception:
            logger.exception("Loi khi cap nhat danh muc id=%s", category.category_id)
            raise

    def delete(self, session: Session, category_id: int) -> bool:
        try:
            entity = self.get_by_id(session, category_id)
            if entity is None:
                return False
            session.delete(entity)
            session.flush()
            return True
        except Exception:
            logger.exception("Loi khi xoa danh muc id=%s", category_id)
            raise