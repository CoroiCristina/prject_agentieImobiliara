from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'

    CNP = Column(String, primary_key=True)
    nume = Column(String)
    prenume = Column(String)
    tel = Column(String)