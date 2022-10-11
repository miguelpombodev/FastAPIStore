from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.engine import URL
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import dotenv_values

envs = dotenv_values()
print(envs)

connection_string = URL.create(
    drivername=envs["DB_DRIVERNAME"],
    username=envs["DB_USERNAME"],
    password=envs["DB_PSWD"],
    host=envs["DB_HOST"],
    port=envs["DB_PORT"],
    database=envs["DB_NAME"],
    query={
        "driver": envs["DB_QUERY"]
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
