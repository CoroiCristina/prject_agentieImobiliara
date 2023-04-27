from pydantic import BaseModel


class pierderi(BaseModel):
    data: str
    suma: float


def venit_vanzari(lista_vanzari: list) -> int:
    suma_v = 0
    for v in lista_vanzari:
        suma_v += v.suma_incasata
    return suma_v


def venit_inchirieri(lista_inchirieri: list) -> int:
    suma_i = 0
    for i in lista_inchirieri:
        suma_i += i.bani_incasati
    return suma_i


def pierderi_administratie(lista_pierderi: list) -> int:
    suma_p = 0
    for p in lista_pierderi:
        suma_p += p.suma
    return suma_p


def calcul_sumaCurentaInCont(lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list, nr_complexe: int) -> int:
    suma_v = venit_vanzari(lista_vanzari)
    suma_i = venit_inchirieri(lista_inchirieri)
    suma_p = pierderi_administratie(lista_pierderi)
    suma_curenta = suma_v + suma_i - suma_p - 1000000*nr_complexe
    return suma_curenta


def minimApartamenteVandute(suma: int) -> None:  # principiu de calcul asemanator cu cel din problema cu pachete(starter, standart,...)
    minimG = round((((suma*32.8)/100)/1500)/22.5)  # 32,8-procentajul reprezentat de garsoniere dintr-un complex, 1500-pret mp, 22,5- medie metraj
    minimAp2 = round((((suma*32.8)/100)/1500)/50)  # 32,8- procentaj apartamente2Camere, 1500-pret mp, 50- medie metraj
    minimAp3 = round((((suma*32.8)/100)/1500)/80)  # 32,8- procentaj Ap3camere, 1500- pret mp, 80- medie metraj
    minimPh = round((((suma*1.6)/100)/1500)/125)  # 1,6- procentaj Penthouse, 1500- pret mp, 125- medie metraj
    print("Pentru a putea ajunge la suma necesara e nevoie sa se vanda un minim de:" +
          f" {minimG} Garsoniere \n {minimAp2} Apartamente cu 2 Camere\n {minimAp3} Apartamente cu 3 camere\n {minimPh} Penthouse-uri")


def Vizualizare_Profit(lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list, nr_complexe: int) -> None:
    suma_curenta = calcul_sumaCurentaInCont(lista_vanzari, lista_inchirieri, lista_pierderi, nr_complexe)
    if suma_curenta > nr_complexe*1000000:
        print(f"Ati ajuns deja pe profit!!!\n Aveti un profit de {suma_curenta-1000000} euro")
    else:
        print(f"Suma curenta din contul firmei este {suma_curenta}")
        minimApartamenteVandute(nr_complexe*100000+1-suma_curenta)


def Vizualizare_ComplexNou(lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list, nr_complexe: int) -> None:
    suma_curenta = calcul_sumaCurentaInCont(lista_vanzari, lista_inchirieri, lista_pierderi, nr_complexe)
    if suma_curenta > 1000000*(nr_complexe+1):
        print("Aveti deja suma necesara pentru a putea construi un complex nou! ")
    else:
        print(f"Suma curenta este de {suma_curenta}!")
        minimApartamenteVandute(1000000*(nr_complexe+1)-suma_curenta)
