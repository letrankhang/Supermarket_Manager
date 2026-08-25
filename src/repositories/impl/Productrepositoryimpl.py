# File: src/repositories/impl/ProductRepositoryImpl.py
"""Triển khai ProductRepository bằng SQLAlchemy ORM (ANSI, chạy được cả MySQL/SQL Server).
Product KHONG co relationship toi Category (theo yeu cau giu nguyen entity),
nen lay ten danh muc bang outerjoin() thu cong qua category_id thay vi joinedload()."""
from __future__ import annotations

import logging
from typing import List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from src.entities.category import Category
from src.entities.product import Product
from src.repositories.Productrepository import ProductRepository, ProductWithCategoryName

logger = logging.getLogger(__name__)


class ProductRepositoryImpl(ProductRepository):

    def get_by_id(self, session: Session, product_id: int) -> Optional[ProductWithCategoryName]:
        try:
            row = (
                session.query(Product, Category.category_name)
                .outerjoin(Category, Product.category_id == Category.category_id)
                .filter(Product.product_id == product_id)
                .first()
            )
            return tuple(row) if row is not None else None
        except Exception:
            logger.exception("Loi khi lay san pham theo id=%s", product_id)
            raise

    def get_by_barcode(self, session: Session, barcode: str) -> Optional[ProductWithCategoryName]:
        try:
            row = (
                session.query(Product, Category.category_name)
                .outerjoin(Category, Product.category_id == Category.category_id)
                .filter(Product.barcode == barcode)
                .first()
            )
            return tuple(row) if row is not None else None
        except Exception:
            logger.exception("Loi khi lay san pham theo barcode=%s", barcode)
            raise

    def search(
        self,
        session: Session,
        keyword: str = "",
        category_id: Optional[int] = None,
    ) -> List[ProductWithCategoryName]:
        try:
            query = session.query(Product, Category.category_name).outerjoin(
                Category, Product.category_id == Category.category_id
            )
            if keyword:
                like = f"%{keyword}%"
                query = query.filter(
                    or_(Product.product_name.ilike(like), Product.barcode.ilike(like))
                )
            if category_id is not None:
                query = query.filter(Product.category_id == category_id)
            rows = query.order_by(Product.product_name.asc()).all()
            return [tuple(row) for row in rows]
        except Exception:
            logger.exception("Loi khi tim kiem san pham (keyword=%s)", keyword)
            raise

    def list_all(self, session: Session) -> List[ProductWithCategoryName]:
        try:
            rows = (
                session.query(Product, Category.category_name)
                .outerjoin(Category, Product.category_id == Category.category_id)
                .order_by(Product.product_name.asc())
                .all()
            )
            return [tuple(row) for row in rows]
        except Exception:
            logger.exception("Loi khi lay danh sach san pham")
            raise

    def list_low_stock(self, session: Session, threshold: int) -> List[ProductWithCategoryName]:
        try:
            rows = (
                session.query(Product, Category.category_name)
                .outerjoin(Category, Product.category_id == Category.category_id)
                .filter(Product.current_stock <= threshold)
                .order_by(Product.current_stock.asc())
                .all()
            )
            return [tuple(row) for row in rows]
        except Exception:
            logger.exception("Loi khi lay danh sach san pham sap het hang")
            raise

    def create(self, session: Session, product: Product) -> Product:
        try:
            session.add(product)
            session.flush()  # co product_id ngay ma khong can commit tai day
            return product
        except Exception:
            logger.exception("Loi khi tao san pham moi")
            raise

    def update(self, session: Session, product: Product) -> Product:
        try:
            merged = session.merge(product)
            session.flush()
            return merged
        except Exception:
            logger.exception("Loi khi cap nhat san pham id=%s", product.product_id)
            raise

    def delete(self, session: Session, product_id: int) -> bool:
        try:
            entity = session.query(Product).filter(Product.product_id == product_id).first()
            if entity is None:
                return False
            session.delete(entity)
            session.flush()
            return True
        except Exception:
            logger.exception("Loi khi xoa san pham id=%s", product_id)
            raise

    def increase_stock_after_import(
        self,
        session: Session,
        product_id: int,
        quantity: int,
        import_unit_price: float,
    ) -> None:
        try:
            product = (
                session.query(Product)
                .filter(Product.product_id == product_id)
                .with_for_update()
                .first()
            )
            if product is None:
                raise ValueError(f"Khong tim thay san pham id={product_id}")

            old_stock = int(product.current_stock or 0)
            old_avg = float(product.avg_import_price or 0)
            new_stock = old_stock + quantity

            # Gia nhap binh quan gia quyen
            if new_stock > 0:
                new_avg = ((old_stock * old_avg) + (quantity * import_unit_price)) / new_stock
            else:
                new_avg = import_unit_price

            product.current_stock = new_stock
            product.avg_import_price = new_avg
            session.flush()
        except Exception:
            logger.exception(
                "Loi khi cap nhat ton kho sau nhap hang cho product_id=%s", product_id
            )
            raise