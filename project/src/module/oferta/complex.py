import random
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import relationship
from sqlalchemy.orm import column_property
from sqlalchemy.ext.declarative import declarative_base
from module.oferta.apartamente import Apartament, Base

Base = declarative_base()


class Complex(Base):
    __tablename__ = 'complex'

    id_complex = Column(Integer, primary_key=True, autoincrement="auto")
    denumire = Column(String(100))
    strada = Column(String(50))
    nr_blocuri = Column(Integer)
