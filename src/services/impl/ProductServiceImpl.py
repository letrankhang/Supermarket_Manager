# File: src/services/impl/ProductServiceImpl.py
"""Trien khai nghiep vu Quan ly San pham. Nhan vao/tra ra DTO, khong lo Entity ra ngoai."""
from __future__ import annotations

import logging
from typing import List, Optional

from config.settings import POSSettings
from config.database import Database
from src.converter.ProductConverter import ProductConverter
from src.dtos.ProductDTO import CreateProductDTO, ProductDTO, UpdateProductDTO
from src.repositories.impl.Productrepositoryimpl import ProductRepositoryImpl
from src.repositories.Productrepository import ProductRepository
from src.services.ProductService import ProductService

logger = logging.getLogger(__name__)


class ProductServiceImpl(ProductService):

    def __init__(self, repository: Optional[ProductRepository] = None) -> None:
        # Cho phep inject repository khac khi test (mock), mac dinh dung Impl that.
        self._repo: ProductRepository = repository or ProductRepositoryImpl()

    def search_products(
        self, keyword: str = "", category_id: Optional[int] = None
    ) -> List[ProductDTO]:
        try:
            with Database.get_session_ctx() as session:
                rows = self._repo.search(session, keyword, category_id)
                return [ProductConverter.to_dto(e, category_name) for e, category_name in rows]
        except Exception:
            logger.exception("Loi khi tim kiem san pham")
            raise RuntimeError("Khong the tim kiem san pham. Vui long thu lai.")

    def get_all_products(self) -> List[ProductDTO]:
        try:
            with Database.get_session_ctx() as session:
                rows = self._repo.list_all(session)
                return [ProductConverter.to_dto(e, category_name) for e, category_name in rows]
        except Exception:
            logger.exception("Loi khi lay danh sach san pham")
            raise RuntimeError("Khong the tai danh sach san pham. Vui long thu lai.")

    def get_product_by_id(self, product_id: int) -> Optional[ProductDTO]:
        try:
            with Database.get_session_ctx() as session:
                row = self._repo.get_by_id(session, product_id)
                if row is None:
                    return None
                entity, category_name = row
                return ProductConverter.to_dto(entity, category_name)
        except Exception:
            logger.exception("Loi khi lay san pham id=%s", product_id)
            raise RuntimeError("Khong the tai thong tin san pham. Vui long thu lai.")

    def get_low_stock_products(self) -> List[ProductDTO]:
        """Nguong canh bao het hang lay tu config, khong hard-code."""
        try:
            threshold: int = POSSettings.LOW_STOCK_THRESHOLD
            with Database.get_session_ctx() as session:
                rows = self._repo.list_low_stock(session, threshold)
                return [ProductConverter.to_dto(e, category_name) for e, category_name in rows]
        except Exception:
            logger.exception("Loi khi lay danh sach san pham sap het hang")
            raise RuntimeError("Khong the tai danh sach san pham sap het hang.")

    def create_product(self, dto: CreateProductDTO) -> ProductDTO:
        self._validate_product_input(dto.barcode, dto.product_name, dto.unit, dto.retail_price)
        try:
            with Database.get_session_ctx() as session:
                existing = self._repo.get_by_barcode(session, dto.barcode)
                if existing is not None:
                    raise ValueError(f"Ma vach '{dto.barcode}' da ton tai.")

                entity = ProductConverter.to_entity_for_create(dto)
                created = self._repo.create(session, entity)
                return ProductConverter.to_dto(created)
        except ValueError:
            raise
        except Exception:
            logger.exception("Loi khi tao san pham moi")
            raise RuntimeError("Khong the tao san pham. Vui long thu lai.")

    def update_product(self, dto: UpdateProductDTO) -> ProductDTO:
        self._validate_product_input(dto.barcode, dto.product_name, dto.unit, dto.retail_price)
        try:
            with Database.get_session_ctx() as session:
                row = self._repo.get_by_id(session, dto.product_id)
                if row is None:
                    raise ValueError(f"Khong tim thay san pham id={dto.product_id}.")
                entity, _ = row

                duplicate = self._repo.get_by_barcode(session, dto.barcode)
                if duplicate is not None and duplicate[0].product_id != dto.product_id:
                    raise ValueError(f"Ma vach '{dto.barcode}' da duoc dung boi san pham khac.")

                ProductConverter.apply_update(entity, dto)
                updated = self._repo.update(session, entity)
                return ProductConverter.to_dto(updated)
        except ValueError:
            raise
        except Exception:
            logger.exception("Loi khi cap nhat san pham id=%s", dto.product_id)
            raise RuntimeError("Khong the cap nhat san pham. Vui long thu lai.")

    def delete_product(self, product_id: int) -> bool:
        try:
            with Database.get_session_ctx() as session:
                return self._repo.delete(session, product_id)
        except Exception:
            logger.exception("Loi khi xoa san pham id=%s", product_id)
            raise RuntimeError(
                "Khong the xoa san pham. San pham co the dang duoc tham chieu boi "
                "hoa don/phieu nhap."
            )

    @staticmethod
    def _validate_product_input(
        barcode: str, product_name: str, unit: str, retail_price: float
    ) -> None:
        if not barcode or not barcode.strip():
            raise ValueError("Ma vach khong duoc de trong.")
        if not product_name or not product_name.strip():
            raise ValueError("Ten san pham khong duoc de trong.")
        if not unit or not unit.strip():
            raise ValueError("Don vi tinh khong duoc de trong.")
        if retail_price < 0:
            raise ValueError("Gia ban le khong duoc am.")