import datetime

from api.modules.base.model import BaseModel

class ProductBrand(BaseModel):
    id: int
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime