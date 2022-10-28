import datetime

from api.modules.base.model import BaseModel

class ProductColors(BaseModel):
    id: str
    product_id: str
    name: str
    product_color_URL: str
    created_at: datetime.datetime
    updated_at: datetime.datetime