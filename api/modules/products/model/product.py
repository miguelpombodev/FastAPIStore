import datetime

from pydantic import BaseModel


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

    @staticmethod
    def __to_dict__(raw_object: object):
        return {
            "id": raw_object.id,
            "type_id": raw_object.type_id,
            "brand_id": raw_object.brand_id,
            "sku": raw_object.sku,
            "name": raw_object.name,
            "value": raw_object.value,
            "stock_amount": raw_object.stock_amount,
            "created_at": raw_object.created_at,
            "updated_at": raw_object.updated_at,
        }
