from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base


# list the path of db file (Sql Lite)
SQLALCHEMY_DATABASE_URL = "sqlite:///../userDb.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})

# creating database session
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# creating Base model class
Base = declarative_base()


