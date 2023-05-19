from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'

    CNP = Column(String(13), primary_key=True)
    nume = Column(String(50))
    prenume = Column(String(50))
    tel = Column(String(10))


def preluareDateClient():
    nume = input("Nume>")
    prenume = input("Prenume>")
    cnp = input("CNP>")
    telefon = input("numar de telefon>")
    return Client(CNP=cnp, nume=nume, prenume=prenume, tel=telefon)
