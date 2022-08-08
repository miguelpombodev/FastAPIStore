from sqlalchemy import Table
from ....shared.providers.database.config import Base, engine


class Product(Base):
    __table__ = Table('products', Base.metadata,
                      autoload=True, autoload_with=engine)

    @classmethod
    def getProducts(cls):
        return cls.query.first()
