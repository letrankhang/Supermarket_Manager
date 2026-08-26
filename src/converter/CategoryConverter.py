from src.dtos.CategoryDTO import CategoryDTO, CreateCategoryDTO, UpdateCategoryDTO
from src.entities.category import Category


class CategoryConverter:
    @staticmethod
    def to_dto(entity: Category) -> CategoryDTO:
        return CategoryDTO(
            category_id=entity.category_id,
            category_name=entity.category_name,
            description=entity.description,
            created_at=entity.created_at,
        )


    @staticmethod
    def to_entity_for_create(dto: CreateCategoryDTO) -> Category:
        return Category(
            category_name=dto.category_name,
            description=dto.description,
        )


    @staticmethod
    def apply_update(entity: Category, dto: UpdateCategoryDTO) -> Category:
        entity.category_name = dto.category_name
        entity.description = dto.description
        return entity