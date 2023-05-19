from datetime import date
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Inregistrare_contBancar(Base):
    __tablename__ = 'cont_bancar'

    cod_inregistrare = Column(Integer, primary_key=True)
    data = Column(String(10))
    suma = Column(Integer)
    detalii = Column(String(50))

# def venit_vanzari(lista_vanzari: list, lista_contracte: list) -> int:
#     suma_v = 0
#     for v in lista_vanzari:
#         suma_v += v.suma_incasata
#     return suma_v


# def venit_inchirieri(lista_inchirieri: list) -> int:
#     suma_i = 0
#     for i in lista_inchirieri:
#         suma_i += i.bani_incasati
#     return suma_i


# def pierderi_administratie(lista_pierderi: list) -> int:
#     suma_p = 0
#     for p in lista_pierderi:
#         suma_p += p.suma
#     return suma_p


def calcul_sumaCurentaInCont(lista_cont: list, lista_complexe: list) -> int:
    suma_curenta = 0
    for i in lista_cont:
        suma_curenta += i.suma
    return suma_curenta - len(lista_complexe)*1000000


def minimApartamenteVandute(suma: int) -> None:  # principiu de calcul asemanator cu cel din problema cu pachete(starter, standart,...)
    minimG = round((((suma*32.8)/100)/1500)/22.5)  # 32,8-procentajul reprezentat de garsoniere dintr-un complex, 1500-pret mp, 22,5- medie metraj
    minimAp2 = round((((suma*32.8)/100)/1500)/50)  # 32,8- procentaj apartamente2Camere, 1500-pret mp, 50- medie metraj
    minimAp3 = round((((suma*32.8)/100)/1500)/80)  # 32,8- procentaj Ap3camere, 1500- pret mp, 80- medie metraj
    minimPh = round((((suma*1.6)/100)/1500)/125)  # 1,6- procentaj Penthouse, 1500- pret mp, 125- medie metraj
    print("Pentru a putea ajunge la suma necesara e nevoie sa se vanda un minim de:" +
          f" {minimG} Garsoniere \n {minimAp2} Apartamente cu 2 Camere\n {minimAp3} Apartamente cu 3 camere\n {minimPh} Penthouse-uri")


def Vizualizare_Profit(lista_cont: list, lista_complexe: list) -> None:
    suma_curenta = calcul_sumaCurentaInCont(lista_cont, lista_complexe)
    if suma_curenta > len(lista_complexe)*1000000:
        print(f"Ati ajuns deja pe profit!!!\n Aveti un profit de {suma_curenta-1000000} euro")
    else:
        print(f"Suma curenta din contul firmei este {suma_curenta}")
        minimApartamenteVandute(len(lista_complexe)*100000+1-suma_curenta)


def Vizualizare_ComplexNou(lista_cont: list, lista_complexe: list) -> None:
    suma_curenta = calcul_sumaCurentaInCont(lista_cont, lista_complexe)
    if suma_curenta > 1000000*(len(lista_complexe)+1):
        print("Aveti deja suma necesara pentru a putea construi un complex nou! ")
    else:
        print(f"Suma curenta este de {suma_curenta}!")
        minimApartamenteVandute(1000000*(len(lista_complexe)+1)-suma_curenta)
