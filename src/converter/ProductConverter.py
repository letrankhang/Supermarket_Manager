from typing import Optional

from src.dtos.ProductDTO import CreateProductDTO, ProductDTO, UpdateProductDTO
from src.entities.product import Product


class ProductConverter:
    @staticmethod
    def to_dto(entity: Product, category_name: Optional[str] = None) -> ProductDTO:
        return ProductDTO(
            product_id=entity.product_id,
            barcode=entity.barcode,
            product_name=entity.product_name,
            category_id=entity.category_id,
            category_name=category_name,
            unit=entity.unit,
            retail_price=float(entity.retail_price or 0),
            current_stock=int(entity.current_stock or 0),
            avg_import_price=float(entity.avg_import_price or 0),
            image=entity.image,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


    @staticmethod
    def to_entity_for_create(dto: CreateProductDTO) -> Product:
        return Product(
            barcode=dto.barcode,
            product_name=dto.product_name,
            category_id=dto.category_id,
            unit=dto.unit,
            retail_price=dto.retail_price,
            current_stock=0,
            avg_import_price=0,
            image=dto.image,
        )


    @staticmethod
    def apply_update(entity: Product, dto: UpdateProductDTO) -> Product:
        entity.barcode = dto.barcode
        entity.product_name = dto.product_name
        entity.category_id = dto.category_id
        entity.unit = dto.unit
        entity.retail_price = dto.retail_price
        entity.image = dto.image
        return entity