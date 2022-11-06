from ...shared.providers.database.config import DBSession

class BaseRepository:
    def __init__(self) -> None:
        self.session = DBSession
