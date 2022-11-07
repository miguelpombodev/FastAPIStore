from sqlalchemy import (
    Column,
    NVARCHAR,
    INTEGER
)
from sqlalchemy.orm import relationship

from api.shared.providers.database.config import Base

class ProductType(Base):
    __tablename__ = "product_type"

    id = Column(INTEGER, primary_key=True)
    description = Column(NVARCHAR(50), nullable=False)
    name = Column(NVARCHAR(40), nullable=False)
    created_at = Column(NVARCHAR(200), nullable=False)
    updated_at = Column(NVARCHAR(200), nullable=False)

    product = relationship("Product", back_populates="product_type", lazy=True)
