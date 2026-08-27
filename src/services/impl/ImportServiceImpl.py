import logging
from typing import List, Optional

from config.database import Database
from src.converter.ImportConverter import ImportConverter
from src.dtos.ImportDTO import CreateImportOrderDTO, ImportOrderDTO
from src.entities.import_detail import ImportDetail
from src.entities.import_order import ImportOrder
from src.entities.product import Product
from src.repositories.impl.Importrepositoryimpl import ImportRepositoryImpl
from src.repositories.impl.Productrepositoryimpl import ProductRepositoryImpl
from src.repositories.Importrepository import ImportRepository
from src.repositories.Productrepository import ProductRepository
from src.services.ImportService import ImportService


logger = logging.getLogger(__name__)

class ImportServiceImpl(ImportService):
    def __init__(
        self,
        import_repository: Optional[ImportRepository] = None,
        product_repository: Optional[ProductRepository] = None,
    ) -> None:
        self._import_repo = (
            import_repository or ImportRepositoryImpl()
        )
        self._product_repo = (
            product_repository or ProductRepositoryImpl()
        )


    def create_import_order(
        self,
        dto: CreateImportOrderDTO
    ) -> ImportOrderDTO:

        self._validate_create_input(dto)

        try:
            with Database.get_session_ctx() as session:

                total_amount = 0.0

                for line in dto.lines:

                    product = (
                        session.query(Product)
                        .filter(
                            Product.product_id == line.product_id
                        )
                        .first()
                    )

                    if not product:
                        raise ValueError(
                            f"Không tìm thấy sản phẩm ID "
                            f"{line.product_id}."
                        )

                    retail_price = float(
                        product.retail_price or 0
                    )
                    if line.unit_price > retail_price:
                        raise ValueError(
                            f"Sản phẩm '{product.product_name}': "
                            f"giá nhập ({line.unit_price:,.0f} VNĐ) "
                            f"không được cao hơn giá bán hiện tại ({retail_price:,.0f} VNĐ)."
                        )

                    total_amount += (
                        line.quantity * line.unit_price
                    )

                order = ImportOrder(
                    supplier_id=dto.supplier_id,
                    user_id=dto.user_id,
                    note=dto.note,
                    total_amount=total_amount,
                )

                created_order = self._import_repo.create(
                    session,
                    order
                )

                for line in dto.lines:

                    detail = ImportDetail(
                        import_id=created_order.import_id,
                        product_id=line.product_id,
                        quantity=line.quantity,
                        unit_price=line.unit_price,
                    )

                    session.add(detail)

                    self._product_repo.increase_stock_after_import(
                        session,
                        product_id=line.product_id,
                        quantity=line.quantity,
                        import_unit_price=line.unit_price,
                    )

                session.flush()

                full_order = self._import_repo.get_by_id(
                    session,
                    created_order.import_id
                )

                return ImportConverter.order_to_dto(
                    full_order
                )

        except ValueError:
            raise

        except Exception as exc:
            logger.exception(
                "Lỗi khi tạo phiếu nhập hàng"
            )
            raise RuntimeError(
                "Không thể tạo phiếu nhập hàng. "
                "Vui lòng thử lại."
            ) from exc


    def get_all_import_orders(
        self
    ) -> List[ImportOrderDTO]:

        try:
            with Database.get_session_ctx() as session:

                entities = self._import_repo.list_all(
                    session
                )

                return [
                    ImportConverter.order_to_dto(entity)
                    for entity in entities
                ]

        except Exception as exc:
            logger.exception(
                "Lỗi khi lấy danh sách phiếu nhập"
            )

            raise RuntimeError(
                "Không thể tải danh sách phiếu nhập hàng."
            ) from exc


    @staticmethod
    def _validate_create_input(
        dto: CreateImportOrderDTO
    ) -> None:

        if dto.supplier_id is None:
            raise ValueError(
                "Vui lòng chọn nhà cung cấp."
            )


        if not dto.lines:
            raise ValueError(
                "Phiếu nhập phải có ít nhất một sản phẩm."
            )

        for line in dto.lines:

            if line.quantity <= 0:
                raise ValueError(
                    "Số lượng nhập phải lớn hơn 0."
                )

            if line.unit_price < 0:
                raise ValueError(
                    "Đơn giá nhập không được âm."
                )