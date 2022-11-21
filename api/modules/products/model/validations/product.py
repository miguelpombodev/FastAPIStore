import datetime
from pydantic import Field

from .product_brand import ProductBrand
from .product_colors import ProductColors
from .product_type import ProductType

from api.modules.base.validation_model import BaseModel

class Product(BaseModel):
    id: str | None = Field(default=None)
    type_id: int
    brand_id: int
    sku: str
    name: str
    value: float
    stock_amount: int

class FullDetailProduct(Product):
    
    product_brand: ProductBrand
    product_colors: list[ProductColors] 
    product_type: ProductType 

    @staticmethod
    def serialize_dict(brand: object, colors_list: list[object], type: object):
        product_brands = ProductBrand(**brand.__dict__)
        product_colors = [ProductColors(**colors.__dict__) for colors in colors_list]
        product_type = ProductType(**type.__dict__) 

        return product_brands, product_type, product_colors
    