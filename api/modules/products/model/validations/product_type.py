import datetime
from api.modules.base.validation_model import BaseModel

class ProductType(BaseModel):
    id: int
    description: str
    name: str