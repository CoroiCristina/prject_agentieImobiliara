from datetime import datetime
from sqlalchemy import (Column,
                        Integer,
                        String)
from sqlalchemy.ext.declarative import declarative_base
from module.oferta.clienti import preluareDateClient
from module.oferta.dataBaseAcces import DBAccess
from module.oferta.contracte import Contract, generate_contract_number
from module.oferta.apartamente import Apartament

Base = declarative_base()


class Inchiriere(Base):
    __tablename__ = 'inchiriere'

    cod_in = Column(Integer, primary_key=True, autoincrement="auto")
    nr_contract = Column(Integer)
    data_intrare = Column(String(10))
    data_iesire = Column(String(10))
    nr_persoane = Column(Integer)
    suma_chirie = Column(Integer)
    nr_plati_ramase = Column(Integer)
    zi_plata = Column(String(2))

    # def __str__(self) -> str:
    #     return (f"{self.data_intrare},{self.data_iesire},{self.apartament},{self.nr_persoane}")


def stabilirePret_luna(nr_persoane) -> int:
    if nr_persoane == 1:
        pret = 100/5  # Curs euro
        return pret
    elif nr_persoane == 2:
        pret = 200/5
        return pret
    elif nr_persoane == 3 or nr_persoane == 4:
        pret = 350/5
        return pret
    elif nr_persoane >= 5:
        pret = 600/5
        return pret


def perioada_de_timp(data_intrare, data_iesire) -> int:
    # convertim datele intr-un format datetime
    data_intrare = datetime.strptime(data_intrare, '%Y-%m-%d')
    data_iesire = datetime.strptime(data_iesire, '%Y-%m-%d')
    # calculam diferenta dintre anii celor doua date
    dif_an = data_iesire.year - data_intrare.year
    # calculam numarul de zile dintre data de intrare si 1 ianuarie a anului de intrare
    zile_intrare = (data_intrare - datetime(data_intrare.year, 1, 1)).days
    if data_intrare.year % 4 == 0:
        zile_intrare += 1

    # calculam numarul de zile dintre data de iesire si 1 ianuarie a anului de iesire
    zile_iesire = (data_iesire - datetime(data_iesire.year, 1, 1)).days
    if data_iesire.year % 4 == 0:
        zile_iesire += 1

    # calculam perioada de timp in zile
    perioada_in_zile = dif_an * 365 + (data_iesire.year // 4 - data_intrare.year // 4) + zile_iesire - zile_intrare
    # calcul perioada de timp in luni
    perioada_in_luni = round(perioada_in_zile/30)
    return perioada_in_luni

    def incasare_chirie(self) -> int:
        perioada = self.perioada_de_timp(self.data_intrare, str(datetime.today().date()))
        bani_incasati = perioada*self.suma_chirie
        return bani_incasati
        # Aceasta functie ar trebui facuta ca un proces aparte care sa verifice in fiecare zi de plata a lunii daca au intrat
        # banii in contul agentiei, iar daca nu sa trimita o avertizare chiriasului si agentiei


def filtruInchirieri(lista_complexe: list, lista_apartamente: list):
    opt = input("Doriti sa aplicati un filtru pentru a putea vedea datele mai usor?")
    if opt.capitalize() == "Da":
        strada = input("Introduceti strada ce va intereseaza:").capitalize()
        for c in lista_complexe:
            if strada == c.strada:
                for ap in lista_apartamente:
                    if ap.id_complex == c.id_complex and ap.bloc_vanzare == 0 and ap.statut == "free":
                        print(str(ap))
    else:
        for ap in lista_apartamente:
            for c in lista_complexe:
                if ap.bloc_vanzare == 0 and ap.id_complex == c.id_complex:
                    print(str(ap), "f Strada: {c.strada}")


def inchiriere(lista_complexe: list, lista_apartamente: list, lista_inchirieri: list, lista_clienti: list, lista_contracte: list, db: DBAccess):
    filtruInchirieri(lista_complexe, lista_apartamente)
    if input("Doriti sa inregistrati o inchiriere?").capitalize() == "Da":
        client = preluareDateClient()
        count = 0
        for cl in lista_clienti:
            if cl.CNP == client.CNP:
                count = 1
        if count == 1:
            db.inserare_DB(client)
            lista_clienti.append(client)
        id_cod = int(input("Introduceti ID-ul apartamentului ce va fi inchiriat:"))
        nr_persoane = int(input("Introduceti numarul de persoane:"))
        data_intrare = input("introduceti data de intrare a locatarilor (format %Y-%m-%d):")
        data_iesire = input("Introduceti data de iesire a locatarilor(format %Y-%m-%d):")
        zi_plata = input("Introduceti ziua din luna in care se va efectua plata:")
        apartament = None
        for ap in lista_apartamente:
            if ap.id_ap == id_cod and ap.bloc_vanzare != 1 and ap.statut == "free":
                apartament = ap
        if apartament is not None:
            ct = Contract(nr_contract=str(len(lista_contracte)+1000001), tip_ct="Inchiriere", cnp=client.CNP, id_ap=apartament.id_ap, id_op=0)
            db.inserare_DB(ct)
            lista_contracte.append(ct)
            inregistrareInchiriere(lista_inchirieri, apartament, nr_persoane, data_intrare, data_iesire, zi_plata, ct, db)
        else:
            print("Apartament indisponibil!")

def inregistrareInchiriere(lista_inchirieri: list, apartament: Apartament, nr_persoane: int, data_intrare: str, data_iesire: str,zi_plata: str, ct: Contract, db: DBAccess):
    lista_inchirieri.append(Inchiriere(cod_in=len(lista_inchirieri)+1, nr_contract=ct.nr_contract, data_intrare=data_intrare, data_iesire=data_iesire, nr_persoane=nr_persoane,
                                       suma_chirie=stabilirePret_luna(nr_persoane), nr_plati_ramase=perioada_de_timp(data_intrare, data_iesire), zi_plata=zi_plata))
    db.inserare_DB(lista_inchirieri[-1])
    apartament.statut = "Inchiriat"
    db.update_ApartamentDB(Apartament, apartament.id_ap, apartament.statut)
    print("Date inregistrate cu succes!")