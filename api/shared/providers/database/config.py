from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import dotenv_values

envs = dotenv_values()

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

def init_ORM():
    connection_string = URL.create(
        drivername=envs["DB_DRIVERNAME"],
        username=envs["DB_USERNAME"],
        password=envs["DB_PSWD"],
        host=envs["DB_HOST"],
        port=envs["DB_PORT"],
        database=envs["DB_NAME"],
        query={"driver": envs["DB_QUERY"]},
    )
    
    engine = create_engine(connection_string)
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)


