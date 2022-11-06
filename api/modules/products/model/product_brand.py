from sqlalchemy import (
    Column,
    NVARCHAR,
    INTEGER
)
from sqlalchemy.orm import relationship

from api.shared.providers.database.config import Base

class ProductBrand(Base):
    __tablename__ = "product_brand"

    id = Column(INTEGER, primary_key=True)
    name = Column(NVARCHAR(40), nullable=False)
    created_at = Column(NVARCHAR(200), nullable=False)
    updated_at = Column(NVARCHAR(200), nullable=False)

    product = relationship("Product", back_populates="product_brand", lazy=True)