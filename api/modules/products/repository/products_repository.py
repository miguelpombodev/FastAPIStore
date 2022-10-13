from ...base.repository import BaseRepository


class ProductsRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(tablename="products")

    pass
