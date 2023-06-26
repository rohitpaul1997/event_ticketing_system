from sqlalchemy import Column, Integer, String
from dbConn import *



# creating user model
class Users(Base):
   __tablename__ = 'Users'
   id = Column(Integer, primary_key=True, autoincrement = True)
   email = Column(String(50), unique=True)
   password = Column(String(50))
   Base.metadata.create_all(bind=engine)