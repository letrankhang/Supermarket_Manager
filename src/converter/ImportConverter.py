from typing import Optional

from src.dtos.ImportDTO import ImportDetailDTO, ImportOrderDTO
from src.entities.import_order import ImportOrder
from src.entities.import_detail import ImportDetail


class ImportConverter:
    @staticmethod
    def detail_to_dto(entity: ImportDetail) -> ImportDetailDTO:
        product_name = entity.product.product_name if getattr(entity, "product", None) else None
        return ImportDetailDTO(
            product_id=entity.product_id,
            product_name=product_name,
            quantity=int(entity.quantity or 0),
            unit_price=float(entity.unit_price or 0),
        )


    @staticmethod
    def order_to_dto(entity: ImportOrder) -> ImportOrderDTO:
        supplier_name = entity.supplier.company_name if getattr(entity, "supplier", None) else None
        user_name = None
        if getattr(entity, "user", None):
            user_name = entity.user.full_name or entity.user.username
        details_dto = [ImportConverter.detail_to_dto(d) for d in (entity.details or [])]
        return ImportOrderDTO(
            import_id=entity.import_id,
            supplier_id=entity.supplier_id,
            supplier_name=supplier_name,
            user_id=entity.user_id,
            import_date=entity.import_date,
            total_amount=float(entity.total_amount or 0),
            note=entity.note,
            details=details_dto,
            user_name=user_name,
        )
