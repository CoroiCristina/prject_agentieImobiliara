from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Apartament(Base):
    __tablename__ = 'complex'

    id_ap = Column(Integer, primary_key=True, autoincrement="auto")
    id_complex = Column(int)
    nr_bloc = Column(int)
    nr_etaj = Column(int)
    nr_ap = Column(int)
    tip_ap = Column(String)
    dimensiune = Column(int)
    bloc_vanzare = Column(int)
    status = Column(String)


def angajat_fals(nr_bloc: int) -> int:
    global bloc_vanzare
    if nr_bloc != 1:
        bloc_vanzare = 0
    else:
        bloc_vanzare = 1
    return bloc_vanzare
