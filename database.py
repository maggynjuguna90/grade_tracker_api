from sqlalchemy import create_engine #function that  creates the connection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./grades.db" #tells sqlalchemy where exactly our db lives

#the actual connection to the database .it uses the url to know where to connect
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
 
#blueprint for creating sessions
SessionLocal = sessionmaker(autoflush=False,autocommit = False,bind = engine)

#parent class for all our database models. class Students(Base) sqlalchemy knows studen is database table
Base = declarative_base()

def get_db():
    db = SessionLocal() #creates fresh db session
    try:
        yield db #gives the session to whoever called get_db and PAUSES here
    finally:
        db.close() #closes the session and returns connection.cleanup happens
        