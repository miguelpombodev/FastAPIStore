from ..repository.products_repository import ProductsRepository


class GetProductByIDService:
    def __init__(self) -> None:
        self._repository = ProductsRepository()

    def execute(self, product_id: str):
        return self._repository.get_by_id(product_id)
