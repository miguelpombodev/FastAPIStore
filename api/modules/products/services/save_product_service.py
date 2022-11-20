from datetime import datetime
import uuid

from ..repository.products_repository import ProductsRepository
from ..model.validations import Product

from api.shared.errors import ServiceError

class SaveProductService:
    def __init__(self) -> None:
        self._repository = ProductsRepository()

    def execute(self, product: Product):
        try:
            check_product = self._repository.get_by_name(product.name)

            if check_product:
                raise ServiceError("Product already saved")

            full_product = self.__add_UUID_timestamp(product)

            return self._repository.save(full_product)
        except ServiceError as e:
            raise ServiceError(e.message)
        except Exception as e:
            raise ServiceError(e)

    def __add_UUID_timestamp(self, product: dict):
        product.id = uuid.uuid4()
        product.created_at = datetime.utcnow()
        product.updated_at = datetime.utcnow()

        return product