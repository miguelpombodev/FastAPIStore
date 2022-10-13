from ...shared.providers.database.config import session, Base


class BaseRepository:
    def __init__(self, tablename: str) -> None:
        self.table = Base.classes.get(tablename)

    def get_by_id(self, id: str):
        return session.query(self.table).filter(self.table.id == id)

    def get_all(self):
        return session.query(self.table).all()
