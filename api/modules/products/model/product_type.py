import datetime

from api.modules.base.model import BaseModel

class ProductType(BaseModel):
    id: int
    description: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime