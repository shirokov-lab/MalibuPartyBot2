from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    chat_id = Column(Integer)
    is_payed = Column(Boolean,default=False) # how

class PicturesTruth(Base):
    __tablename__ = 'truths'
    id = Column(Integer, primary_key = True)
    filename = Column(String)
    file_id = Column(String)


class PicturesAction(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key = True)
    filename = Column(String)
    file_id = Column(String)