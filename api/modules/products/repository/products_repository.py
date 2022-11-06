from sqlalchemy.orm import contains_eager

from api.shared.providers.database.config import Base
from api.modules.products.model import Product,ProductColors

from ...base.repository import BaseRepository

class ProductsRepository(BaseRepository):

    def get_by_id(self, id: str):
        product: Product = (self.session.query(Product)
                               .join(Product.product_type)
                               .join(Product.product_brand)
                               .filter(Product.id == id)
                               .options(contains_eager(Product.product_type))
                               .options(contains_eager(Product.product_brand))
                               .first())

        product.product_colors = (self.session.query(ProductColors).filter(ProductColors.product_id == id).all())

        return product

    def get_all(self) -> list[Product]:
        products: list[Product] = (self.session.query(Product)
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
