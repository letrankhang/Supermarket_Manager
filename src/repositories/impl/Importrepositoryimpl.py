import logging
from typing import List, Optional

from sqlalchemy.orm import Session, joinedload, selectinload

from src.entities.import_order import ImportOrder
from src.repositories.Importrepository import ImportRepository

logger = logging.getLogger(__name__)


class ImportRepositoryImpl(ImportRepository):
    def create(self, session: Session, order: ImportOrder) -> ImportOrder:
        try:
            session.add(order)
            session.flush() 
            return order
        except Exception:
            logger.exception("Loi khi tao phieu nhap hang")
            raise


    def get_by_id(self, session: Session, import_id: int) -> Optional[ImportOrder]:
        try:
            return (
                session.query(ImportOrder)
                .options(
                    joinedload(ImportOrder.supplier),
                    joinedload(ImportOrder.user),
                    selectinload(ImportOrder.details),
                )
                .filter(ImportOrder.import_id == import_id)
                .first()
            )
        except Exception:
            logger.exception("Loi khi lay phieu nhap id=%s", import_id)
            raise


    def list_by_supplier(self, session: Session, supplier_id: int) -> List[ImportOrder]:
        try:
            return (
                session.query(ImportOrder)
                .options(
                    joinedload(ImportOrder.supplier),
                    joinedload(ImportOrder.user),
                    selectinload(ImportOrder.details),
                )
                .filter(ImportOrder.supplier_id == supplier_id)
                .order_by(ImportOrder.import_date.desc())
                .all()
            )
        except Exception:
            logger.exception("Loi khi lay phieu nhap theo supplier_id=%s", supplier_id)
            raise


    def list_all(self, session: Session) -> List[ImportOrder]:
        try:
            return (
                session.query(ImportOrder)
                .options(
                    joinedload(ImportOrder.supplier),
                    joinedload(ImportOrder.user),
                    selectinload(ImportOrder.details),
                )
                .order_by(ImportOrder.import_date.desc())
                .all()
            )
        except Exception:
            logger.exception("Loi khi lay danh sach phieu nhap")
            raise