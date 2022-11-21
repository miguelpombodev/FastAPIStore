import datetime
from api.modules.base.validation_model import BaseModel

class ProductBrand(BaseModel):
    id: int
    name: str