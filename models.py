from sqlalchemy import Column,Integer,String 
from db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(25),unique=True,nullable=False)
    email = Column(String(30),unique=True,nullable=False)