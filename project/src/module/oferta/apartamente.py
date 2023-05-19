from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Apartament(Base):
    __tablename__ = 'apartament'

    id_ap = Column(Integer, primary_key=True)
    id_complex = Column(Integer)
    nr_bloc = Column(Integer)
    nr_etaj = Column(Integer)
    nr_ap = Column(Integer)
    tip_ap = Column(String(30))
    dimensiune = Column(Integer)
    bloc_vanzare = Column(Integer)
    statut = Column(String(10))
    def __str__(self) -> str:
        return (f"id_ap: {self.id_ap}, id_complex: {self.id_complex}, nr_bloc: {self.nr_bloc}, nr_etaj: {self.nr_etaj}, nr_ap: {self.nr_ap}, tip_ap: {self.tip_ap}, dimensiune: {self.dimensiune}")



def angajat_fals(nr_bloc: int) -> int:
    global bloc_vanzare
    if nr_bloc != 1:
        bloc_vanzare = 0
    else:
        bloc_vanzare = 1
    return bloc_vanzare
