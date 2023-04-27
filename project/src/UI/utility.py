import json
import threading
from module.oferta.tipApartament import (Garsoniera,
                                         Apartament2Camere,
                                         Apartament3Camere,
                                         Penthouse)
from module.servicii.vanzari import (Vanzare,
                                     vanzare)
from module.servicii.inchirieri import (Inchiriere,
                                        inchiriere)
from module.serializare.serializarea import MyEncouder
from module.servicii.contabilitatea import (pierderi,
                                            Vizualizare_Profit,
                                            Vizualizare_ComplexNou)
from module.servicii.thread import myThread


def creareOferta(lista_apartamente: list) -> None:
    try:
        nr_complexe = int(input("Cate complexe doriti sa inregistrati?"))
    except Exception:
        print("Nu ati introdus un tip de data valida! Mai introduceti odata")
        nr_complexe = int(input("Cate complexe doriti sa inregistrati?"))
    for comp in range(nr_complexe):
        try:
            denumire = input("Cum se numeste complexul?")
        except Exception:
            print("Nu ati introdus un tip de data valida! Mai introduceti odata")
            denumire = input("Cum se numeste complexul?")
        try:
            strada = input("Pe ce strada este situat complexul "+str(comp+1)+"?")
        except Exception:
            print("Nu ati introdus un tip de data valida! Mai introduceti odata")
            strada = input("Pe ce strada este situat complexul "+str(comp+1)+"?")
        nr_blocuri = 3
        for bloc in range(nr_blocuri):
            for etaj in range(11):
                if etaj < 10:
                    for i in range(4):
                        lista_apartamente.append(Garsoniera(len(lista_apartamente)+1, denumire, strada, bloc+1, etaj, etaj*100+i+1, "free"))
                        lista_apartamente.append(Apartament2Camere(len(lista_apartamente)+1, denumire, strada, bloc+1, etaj, etaj*100+i+5, "free"))
                        lista_apartamente.append(Apartament3Camere(len(lista_apartamente)+1, denumire, strada, bloc+1, etaj, etaj*100+i+9, "free"))
                    else:
                        for i in range(2):
                            lista_apartamente.append(Penthouse(len(lista_apartamente)+1, denumire, strada, bloc+1, etaj, etaj*100+i+1, "free"))


def decoratorScriereFisier(functie):
    def wrapper(lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list):
        with open("oferta.json", "w") as f:
            for ap in lista_apartamente:
                f.write(json.dumps(ap, cls=MyEncouder)+'\n')
        with open('inchirieri.txt', 'w') as file:
            for i in lista_inchirieri:
                file.write(str(i)+"\n")
        with open('vanzari.txt', 'w') as f:
            for v in lista_vanzari:
                f.write(str(v)+"\n")
        with open("pierderi.txt", 'w')as f:
            for p in lista_pierderi:
                f.write(p.data+"," + str(p.suma)+"\n")
        return functie(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    return wrapper


def citire_fisier(lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list) -> None:
    with open("oferta.json", 'r') as file:
        for line in file:
            lista = json.loads(line.strip())
            if lista[8] == "Garsoniera":
                obj = Garsoniera(int(lista[0]), lista[1], lista[2], int(lista[3]), int(lista[4]),  int(lista[5]), lista[6], int(lista[7]), lista[8])
            elif lista[8] == "Apartament cu 2 camere":
                obj = Apartament2Camere(int(lista[0]), lista[1], lista[2], int(lista[3]), int(lista[4]),  int(lista[5]), lista[6], int(lista[7]), lista[8])
            elif lista[8] == "Apartament cu 3 camere":
                obj = Apartament3Camere(int(lista[0]), lista[1], lista[2], int(lista[3]), int(lista[4]),  int(lista[5]), lista[6], int(lista[7]), lista[8])
            elif lista[8] == "Penthouse":
                obj = Penthouse(int(lista[0]), lista[1], lista[2], int(lista[3]), int(lista[4]),  int(lista[5]), lista[6], int(lista[7]), lista[8])
            lista_apartamente.append(obj)

    with open("vanzari.txt", 'r') as file:
        for line in file:
            lista = line.strip().split(",")
            lista_vanzari.append(vanzare((lista[0]), int(lista[1]), lista[2]))

    with open("inchirieri.txt", 'r') as file:
        for line in file:
            lista = line.strip().split(",")
            lista_inchirieri.append(inchiriere(lista[0], lista[1], int(lista[2]), int(lista[3])))

    with open("pierderi.txt", 'r') as file:
        for line in file:
            lista = line.strip().split(",")
            lista_pierderi.append(pierderi(data=lista[0], suma=int(lista[1])))


def meniu(lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list) -> None:
    lista = [lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi]
    thread = threading.Thread(target=myThread, args=lista)
    thread.start()
    print("1. Efectuare Vanzare")
    print("2. Efectuare Inchiriere")
    print("3. Interogare incasari/profit")
    print("4. Adaugare compex nou")
    print("5. Iesire")

    opt = input(">").strip()
    thread.join()
    if opt == "1":
        submeniu1(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    elif opt == "2":
        submeniu2(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    elif opt == "3":
        submeniu3(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    elif opt == "4":
        submeniu4(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    elif opt == "5":
        iesire(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)


def submeniu1(lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list) -> None:
    print("1. Vizualizare apartamente disponibile + efectuare vanzare")
    print("2. Inapoi")

    opt1 = input(">").strip()
    if opt1 == "1":
        Vanzare(lista_apartamente, lista_vanzari)
        submeniu1(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    elif opt1 == "2":
        meniu(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)


def submeniu2(lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list) -> None:
    print("1. Vizualizare apartamente disponibile + efectuare inchiriere")
    print("2. Inapoi")

    opt1 = input(">").strip()
    if opt1 == "1":
        Inchiriere(lista_apartamente, lista_inchirieri)
        submeniu2(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    elif opt1 == "2":
        meniu(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)


def submeniu3(lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list) -> None:
    print("1. Vizualizare minim apartamente vandute pentru profit")
    print("2. Vizualizare minim apartamnete vandute pentru un complex nou")
    print("3. Inapoi")

    opt1 = input(">").strip()
    if opt1 == "1":
        Vizualizare_Profit(lista_vanzari, lista_inchirieri, lista_pierderi, (len(lista_apartamente)/122)/3)  # 122-nr. ap intr-un bloc, 3 nr bl in complex
        submeniu3(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    elif opt1 == "2":
        Vizualizare_ComplexNou(lista_vanzari, lista_inchirieri, lista_pierderi, (len(lista_apartamente)/122)/3)
        submeniu3(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    elif opt1 == "3":
        meniu(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)


def submeniu4(lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list) -> None:
    if input("Doriti sa inregistrati un complex nou?").capitalize() == "Da":
        creareOferta(lista_apartamente)
        meniu(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    else:
        meniu(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)


@decoratorScriereFisier
def iesire(lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_pierderi: list):
    exit()
