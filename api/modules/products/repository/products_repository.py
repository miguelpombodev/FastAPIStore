from ...base.repository import BaseRepository
from api.modules.products.model import Product


class ProductsRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(tablename="products")

    def get_by_id(self, id: str) -> Product:
        product: object = self.query.filter(self.table.id == id).first()

        return Product(**product.__dict__)

    def get_all(self) -> list[Product]:
        products: list = []
        raw_products = self.query.all()

        for product in raw_products:
            products.append(Product(**product.__dict__))

        return products
