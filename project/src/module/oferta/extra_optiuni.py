from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class extra_optiune(Base):
    __tablename__ = 'extra_optiune'

    id_op = Column(Integer, primary_key=True)
    denumire = Column(String)
    pret = Column(int)


def alegere_extraOP():
    print("Introduceti extra-optiunea aleasa de catre client:")
    for key in extra_optiuni.keys():
        print(key)
    extra_optiune = input(">").capitalize()
    for key in extra_optiuni.keys():
        if key == extra_optiune:
            return extra_optiune[key]
