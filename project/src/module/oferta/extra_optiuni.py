from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class extra_optiune(Base):
    __tablename__ = 'extra_optiune'

    id_op = Column(Integer, primary_key=True)
    denumire = Column(String(50))
    pret = Column(Integer)


def alegere_extraOP(lista_extraOp: list):
    print("Introduceti extra-optiunea aleasa de catre client:")
    for e in lista_extraOp:
        print(e.denumire)
    extra_optiune = input(">").capitalize()
    for e in lista_extraOp:
        if e.denumire == extra_optiune:
            return e
