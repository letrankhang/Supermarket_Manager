from abc import ABC, abstractmethod
from typing import List, Optional

from src.dtos.ImportDTO import CreateImportOrderDTO, ImportOrderDTO

class ImportService(ABC):

    @abstractmethod
    def create_import_order(self, dto: CreateImportOrderDTO) -> ImportOrderDTO:
        pass

    @abstractmethod
    def get_import_order(self, import_id: int) -> Optional[ImportOrderDTO]:
        pass

    @abstractmethod
    def get_all_import_orders(self) -> List[ImportOrderDTO]:
        pass

    @abstractmethod
    def get_import_orders_by_supplier(self, supplier_id: int) -> List[ImportOrderDTO]:
        pass