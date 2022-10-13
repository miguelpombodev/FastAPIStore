from ..repository.products_repository import ProductsRepository


class ListProductsService:
    def __init__(self) -> None:
        self._repository = ProductsRepository()

    def execute(self):
        return self._repository.get_all()
