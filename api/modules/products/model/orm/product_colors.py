from sqlalchemy import (
    Column,
    NVARCHAR,
    ForeignKey
)
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship

from api.shared.providers.database.config import Base


class ProductColors(Base):
    __tablename__ = "product_colors"

    id = Column(UNIQUEIDENTIFIER(), primary_key=True)
    product_id = Column(UNIQUEIDENTIFIER(), ForeignKey('products.id'),nullable=False)
    name = Column(NVARCHAR(25), nullable=False)
    product_color_URL = Column(NVARCHAR(200), nullable=False)
    created_at = Column(NVARCHAR(200), nullable=False)
    updated_at = Column(NVARCHAR(200), nullable=False)

    product = relationship("Product", back_populates="product_colors", lazy=True)