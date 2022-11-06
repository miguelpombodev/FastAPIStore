from sqlalchemy import (
    Column,
    NVARCHAR,
    INTEGER,
    DECIMAL,
    ForeignKey
)
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship


from api.shared.providers.database.config import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(UNIQUEIDENTIFIER(), primary_key=True)
    type_id = Column(INTEGER, ForeignKey("product_type.id"), nullable=False)
    brand_id = Column(INTEGER, ForeignKey("product_brand.id"), nullable=False)
    sku = Column(NVARCHAR(255), nullable=False)
    name = Column(NVARCHAR(15), nullable=False)
    value = Column(DECIMAL(6,2), nullable=False)
    created_at = Column(NVARCHAR(200), nullable=False)
    updated_at = Column(NVARCHAR(200), nullable=False)

    product_type = relationship("ProductType", back_populates="product", lazy=True)
    product_brand = relationship("ProductBrand", back_populates="product", lazy=True)
    product_colors = relationship("ProductColors", back_populates="product", lazy=True, uselist=True)


