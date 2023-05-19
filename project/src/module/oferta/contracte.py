from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import random
from module.oferta.dataBaseAcces import DBAccess

Base = declarative_base()


class Contract(Base):
    __tablename__ = 'contract'

    nr_contract = Column(String(10), primary_key=True)
    tip_ct = Column(String(10))
    cnp = Column(String(13))
    id_ap = Column(Integer)
    id_op = Column(Integer)


def generate_contract_number(db: DBAccess):
    used_contract_numbers = db.ExtragereNrContracteExistente(Contract)
    while True:
        contract_number = random.randint(100000, 999999)  # generăm un număr între 100000 și 999999
        if contract_number not in used_contract_numbers:  # verificăm dacă numărul a fost deja folosit
            used_contract_numbers.add(contract_number)  # adăugăm numărul la setul de numere folosite
            return contract_number
