from ....shared.providers.database.config import session, Base

products = Base.classes.products


class Product():

    @classmethod
    def getProducts(cls):
        return session.query(products).first()
