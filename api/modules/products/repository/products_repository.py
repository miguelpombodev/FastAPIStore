from ...base.repository import BaseRepository
from api.modules.products.model import FullDetailProduct, Product


class ProductsRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(tablename="products")

    def get_by_id(self, id: str):
        product_raw: object = self.query.filter(self.table.id == id).first()

        product = FullDetailProduct(**product_raw.__dict__)
        product.set_brand(product_raw.product_brand)
        product.set_colors(product_raw.product_colors_collection)
        product.set_type(product_raw.product_type)

        return product

    def get_all(self) -> list[Product]:
        return [Product(**product.__dict__) for product in self.query.all()]
