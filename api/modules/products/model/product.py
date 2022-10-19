import datetime

from api.modules.base.model import BaseModel


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
