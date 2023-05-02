from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Complex(Base):
    __tablename__ = 'complex'

    id_complex = Column(Integer, primary_key=True, autoincrement="auto")
    denumire = Column(String)
    strada = Column(String)
    nr_blocuri = Column(int)
    lista_apartamente = Column( nullable=False)
