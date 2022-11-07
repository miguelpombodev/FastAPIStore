from ..repository.products_repository import ProductsRepository

from ..model.validations import Product


class ListProductsService:
    def __init__(self) -> None:
        self._repository = ProductsRepository()

    def execute(self) -> list[Product]:
        orm_result = self._repository.get_all()

        products = [Product(**result.__dict__) for result in orm_result]

        return products
