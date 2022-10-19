from ...shared.providers.database.config import session, Base


class BaseRepository:
    def __init__(self, tablename: str) -> None:
        self.table = Base.classes.get(tablename)
        self.query = session.query(self.table)
