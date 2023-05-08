from datetime import date
from module.oferta.extra_optiuni import (alegere_extraOP,
                                         extra_optiune)
from .Bot import negociere
from sqlalchemy import (Column,
                        Integer,
                        String)
from sqlalchemy.ext.declarative import declarative_base
from module.oferta.contracte import (Contract,
                                     generate_contract_number)
from module.oferta.clienti import preluareDateClient
from module.oferta.dataBaseAcces import DBAccess
from module.oferta.apartamente import Apartament

Base = declarative_base()


class Vanzare(Base):
    __tablename__ = 'vanzare'

    nr_contract = Column(Integer, primary_key=True)
    data = Column(String(10))
    suma = Column(Integer)
    cod_v = Column(Integer)


# class vanzare:
#     def __init__(self, apartament: int, suma_incasata: int, data_vanzare: date = date.today()) -> None:
#         self.apartament = apartament
#         self.suma_incasata = suma_incasata
#         self.data_vanzare = data_vanzare

#     def __str__(self) -> str:
#         return (f"{self.apartament},{self.suma_incasata},{self.data_vanzare}")


def filtru(lista_complexe: list, lista_apartamente: list, db: DBAccess) -> None:
    opt = input("Doriti sa aplicati un filtru pentru a putea vedea datele mai usor?")
    if opt.capitalize() == "Da":
        strada = input("Introduceti strada ce va intereseaza:").capitalize()
        for c in lista_complexe:
            if strada == c.strada:
                for ap in lista_apartamente:
                    if ap.id_complex == c.id_complex and ap.bloc_vanzare == 1 and ap.statut == "free":
                        print(str(ap))
    else:
        for ap in lista_apartamente:
            for c in lista_complexe:
                if ap.bloc_vanzare == 1 and ap.id_complex == c.id_complex:
                    print(str(ap), "f Strada: {c.strada}")


def vanzare(lista_complexe: list, lista_apartamente: list, lista_vanzari: list, lista_clienti: list, lista_contracte: list,lista_extraOp: list, db: DBAccess) -> None:
    filtru(lista_complexe, lista_apartamente, db)
    print("Doriti sa efectuati o vanzare?")
    if input(">").capitalize() == "Da":
        print("Introduceti datele clientului:")
        client = preluareDateClient()
        count = 0
        for cl in lista_clienti:
            if cl.CNP == client.CNP:
                count = 1
        if count != 1:
            db.inserare_DB(client)
            lista_clienti.append(client)
        id_cod = int(input("Introduceti codul apartamentului ce va fi vandut: "))
        apartament= None
        for ap in lista_apartamente:
            if ap.id_ap == id_cod and ap.statut == "free" and ap.bloc_vanzare == 1:
                apartament = ap
        if apartament is not None:
            pret_apartament = apartament.dimensiune*1500  # euro mp
            if pret_apartament > 80000:
                print("Imobilul are deja un potential cumparator, se vor efectua negocieri intre clienti")
                pret_apartament = negociere(pret_apartament, apartament)
                if pret_apartament != 0:
                    extra = alegere_extraOP(lista_extraOp)
                    ct = Contract(nr_contract=str(len(lista_contracte)+1000001), tip_ct="Vanzare", cnp=client.CNP, id_ap=apartament.id_ap, id_op=extra.id_op)
                    db.inserare_DB(ct)
                    lista_contracte.append(ct)
                    inregistrarevanzare(apartament, pret_apartament, lista_vanzari, extra, ct, db)
                else:
                    print("Apartamentul nu va mai fi vandut")
            else:
                print(f"Pretul apartamentului este de {pret_apartament}")
                extra = alegere_extraOP(lista_extraOp)
                ct = Contract(nr_contract=str(len(lista_contracte)+100001), tip_ct="Vanzare", cnp=client.CNP, id_ap=apartament.id_ap, id_op=extra.id_op)
                db.inserare_DB(ct)
                lista_contracte.append(ct)
                inregistrarevanzare(ap, pret_apartament, lista_vanzari, extra, ct, db)
        else:
            print("Apartament indisponibil!")


def inregistrarevanzare(apartament: object, pret_apartament: list, lista_vanzari: list, extra: extra_optiune, ct: Contract, db: DBAccess) -> None:
    pret_final = pret_apartament + extra.pret
    print("Pretul final este ", pret_final, " euro")
    v = Vanzare(nr_contract=ct.nr_contract, data=str(date.today()), suma=pret_final, cod_v=len(lista_vanzari)+1)
    db.inserare_DB(v)
    lista_vanzari.append(v)
    apartament.statut = "Vandut"
    db.update_ApartamentDB(Apartament, apartament.id_ap, apartament.statut)
    print("Date inregistrate cu succes!")
