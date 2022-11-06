from sqlalchemy.orm import contains_eager

from api.shared.providers.database.config import Base
from api.modules.products.model import Product

from ...base.repository import BaseRepository

class ProductsRepository(BaseRepository):

    def get_by_id(self, id: str):
        product = (self.session.query(Product)
                               .join(Product.product_type)
                               .join(Product.product_brand)
                               .filter(Product.id == id)
                               .options(contains_eager(Product.product_type))
                               .options(contains_eager(Product.product_brand))
                               .first())

        return product

    def get_all(self) -> list[Product]:
        products = (self.session.query(Product)
                                .join(Product.product_brand)     
                                .options(contains_eager(Product.product_brand))
                                .all())
        return products

    def save(self, product: Product):
        try:
            ProductMap = Base.classes.products
            mapped_product = ProductMap(**product.__dict__)

            self.session.add(mapped_product)
            self.session.commit()

            return True
        except Exception as e:
            raise Exception(e)
