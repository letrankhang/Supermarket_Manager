from abc import ABC, abstractmethod
from typing import List

from src.dtos.ImportDTO import CreateImportOrderDTO, ImportOrderDTO

class ImportService(ABC):

    @abstractmethod
    def create_import_order(self, dto: CreateImportOrderDTO) -> ImportOrderDTO:
        pass

    @abstractmethod
    def get_all_import_orders(self) -> List[ImportOrderDTO]:
        pass