from datetime import datetime
import uuid

from ..repository.products_repository import ProductsRepository
from ..model import Product

SHA_SECRET: str = "teste"

class SaveProductService:
    def __init__(self) -> None:
        self._repository = ProductsRepository()

    def execute(self, product: Product):
        try:
            full_product = self.__add_UUID_timestamp(product)

            return self._repository.save(full_product)
        except Exception as e:
            raise Exception(e)

    def __add_UUID_timestamp(self, product: dict):
        product.id = uuid.uuid5(uuid.NAMESPACE_URL, SHA_SECRET)
        product.created_at = datetime.utcnow()
        product.updated_at = datetime.utcnow()

        return product