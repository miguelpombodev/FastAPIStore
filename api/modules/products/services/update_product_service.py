from ..repository.products_repository import ProductsRepository

from api.modules.products.model.validations import Product
from api.shared.errors import ServiceError

class UpdateProductService():
    def __init__(self) -> None:
        self._repository = ProductsRepository()

    def execute(self, product_id: str, product: Product) -> dict:
        try:
            existed_product = self._repository.get_by_id(product_id)

            if not existed_product:
                raise ServiceError("Product does not exist")

            update_result = self._repository.update_one(existed_product, product)

            return update_result
        except Exception as e:
            raise ServiceError(e)