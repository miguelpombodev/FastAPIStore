from api.modules.base.validation_model import BaseModel

class ProductColors(BaseModel):
    id: str
    product_id: str
    name: str
    product_color_URL: str