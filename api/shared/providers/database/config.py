from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, engine


connection_string = engine.url.URL(
    "mssql+pyodbc",
    username="sa",
    password="Passw0rd",
    host="localhost",
    database="OnlineStore"
)

print(connection_string)
engine_created = create_engine(connection_string)
# "mssql+pyodbc://sa:P@ssw0rd!@db:1433/OnlineStore?driver=ODBC+Driver+17+for+SQL+Server")

Base = automap_base()
# session = Session(engine_created)
# Base.prepare(autoload_with=engine, reflect=True)

SessionLocal = Session(bind=engine)
