from sqlalchemy.orm import contains_eager

from api.shared.providers.database.config import Base
from api.modules.products.model.orm import Product,ProductColors

from ...base.repository import BaseRepository

class ProductsRepository(BaseRepository):

    def get_detailed_by_id(self, id: str):
        try:
            product: Product = (self.session.query(Product)
                                .join(Product.product_type)
                                .join(Product.product_brand)
                                .filter(Product.id == id)
                                .options(contains_eager(Product.product_type))
                                .options(contains_eager(Product.product_brand))
                                .first())

            product.product_colors = (self.session.query(ProductColors).filter(ProductColors.product_id == id).all())

            return product
        except Exception:
            raise Exception("Product not found")

    def get_by_id(self, id: str):
        try:
            product: Product = (self.session.query(Product)
                                .filter(Product.id == id)
                                .first())

            return product
        except Exception as e:
            raise Exception(e)
    
    def get_by_name(self, name: str):
        try:
            product: Product = (self.session.query(Product)
                                .filter(Product.name == name)
                                .first())

            return product
        except Exception as e:
            raise Exception(e)

    def get_all(self) -> list[Product]:
        try:
            products: list[Product] = (self.session.query(Product)
                                    .all())
            return products
        except Exception as e:
            raise Exception(e)

    def save(self, product: Product):
        try:
            self.session.add(Product(**product.__dict__))
            self.session.commit()

            return True
        except Exception:
            raise Exception("It was not able to save product in database")

    def update_one(self, old_product: Product, new_product):
        try:

            filter = self.session.query(Product).filter(Product.id == old_product.id)

            # @ToDo: Code smell here, better refactor
            values = {key: new_product.__dict__[key] for key in new_product.__dict__ if  key in old_product.__dict__ and new_product.__dict__[key] != old_product.__dict__[key]}

            filter.update(values)

            self.session.commit()
            self.session.flush()

            return {
                "status": "Item updated successfully"
            }
        except Exception as e:
            raise Exception(e)