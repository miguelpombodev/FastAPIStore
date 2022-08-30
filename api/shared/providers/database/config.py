from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.engine import URL
from sqlalchemy.orm import scoped_session, sessionmaker

# from ....modules.Base.Model.base_model import BaseModel

connection_string = URL.create(
    drivername="mssql+pyodbc",
    username="sa",
    password="Passw0rd",
    host="172.18.0.2",
    port=1433,
    database="OnlineStore",
    query={
        "driver": "ODBC Driver 17 for SQL Server"
    }
)


engine = create_engine(connection_string)
session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
))


Base = automap_base()
Base.prepare(engine, reflect=True)
