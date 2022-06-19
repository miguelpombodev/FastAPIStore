import datetime

from pydantic import BaseModel
from uuid import UUID


class Customer(BaseModel):
    id: UUID()
    name: str
    surname: str
    CPF: str
    email: str
    password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
