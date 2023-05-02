from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contract(Base):
    __tablename__ = 'contract'

    nr_contract = Column(String, primary_key=True)
    tip_ct = Column(String)
    cnp = Column(String)
    id_ap = Column(int)
    id_op = Column(int)