from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.engine import URL

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

Base = automap_base()

print(connection_string)

engine = create_engine(connection_string)

print(engine)

Base.prepare(engine, reflect=True)
