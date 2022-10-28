import datetime

from api.modules.base.model import BaseModel
from .product_brand import ProductBrand
from .product_colors import ProductColors
from .product_type import ProductType


class Product(BaseModel):
    id: str
    type_id: int
    brand_id: int
    sku: str
    name: str
    value: float
    stock_amount: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

class FullDetailProduct(Product):
    product_brands: list[ProductBrand] | None = []
    product_colors: list[ProductColors] | None = []
    product_type: list[ProductType] | None = []

    def set_brand(self, brand: object):
        self.product_brands = ProductBrand(**brand.__dict__)

    def set_colors(self, list: list[object]):
        self.product_colors = [ProductColors(**colors.__dict__) for colors in list]

    def set_type(self, type: object):
        self.product_type = ProductType(**type.__dict__)


