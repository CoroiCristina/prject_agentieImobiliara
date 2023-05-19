import threading
import random
from module.servicii.vanzari import (Vanzare,
                                     vanzare)
from module.servicii.inchirieri import (Inchiriere,
                                        inchiriere)
from module.servicii.contabilitatea import (Inregistrare_contBancar,
                                            Vizualizare_Profit,
                                            Vizualizare_ComplexNou)
from module.servicii.thread import myThread
from module.oferta.apartamente import Apartament, angajat_fals
from module.oferta.complex import Complex
from module.oferta.extra_optiuni import extra_optiune
from module.oferta.dataBaseAcces import DBAccess
from module.oferta.clienti import Client
from module.oferta.contracte import Contract

DB = DBAccess()


def verifDate():
    lista_complexe = DB.extragereDateDB(Complex)
    lista_apartamente = DB.extragereDateDB(Apartament)
    lista_extraOp = DB.extragereDateDB(extra_optiune)
    lista_clienti = DB.extragereDateDB(Client)
    lista_contracte = DB.extragereDateDB(Contract)
    lista_vanzari = DB.extragereDateDB(Vanzare)
    lista_inchirieri = DB.extragereDateDB(Inchiriere)
    lista_cont = DB.extragereDateDB(Inregistrare_contBancar)
    if len(lista_complexe) == 0:
        creareComplexeNoi(lista_complexe, lista_apartamente)
    elif len(lista_apartamente) == 0:
        CreareApartamenteNoi(lista_apartamente, lista_complexe)
    if len(lista_extraOp) == 0:
        creareExtraOpNoi()
    meniu(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
          lista_clienti, lista_contracte, lista_cont)


def creareComplexeNoi(Lista_Complexe: list, lista_apartamente: list):
    lista_complexe = []
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
        id_Complex = len(lista_complexe)+1+len(Lista_Complexe)
        lista_complexe.append(Complex(id_complex=id_Complex, denumire=denumire, strada=strada, nr_blocuri=nr_blocuri))
        for c in lista_complexe:
            Lista_Complexe.append(c)
            DB.inserare_DB(c)
        CreareApartamenteNoi(lista_apartamente, lista_complexe)


def CreareApartamenteNoi(Lista_Apartamente: list, lista_complexe: list):
    lista_apartamente = []
    for c in lista_complexe:
        for bloc in range(c.nr_blocuri):
            for etaj in range(11):
                if etaj < 10:
                    for i in range(4):
                        lista_apartamente.append(Apartament(id_ap=len(lista_apartamente)+1+len(Lista_Apartamente), id_complex=c.id_complex, nr_bloc=bloc+1, nr_etaj=etaj, nr_ap=etaj*100+i+1,
                                                            tip_ap="Garsoniera", dimensiune=random.randint(20, 25), bloc_vanzare=angajat_fals(bloc+1), statut="free"))
                        lista_apartamente.append(Apartament(id_ap=len(lista_apartamente)+1+len(Lista_Apartamente), id_complex=c.id_complex, nr_bloc=bloc+1, nr_etaj=etaj, nr_ap=etaj*100+i+5,
                                                            tip_ap="Apartament cu 2 camere", dimensiune=random.randint(40, 60), bloc_vanzare=angajat_fals(bloc+1), statut="free"))
                        lista_apartamente.append(Apartament(id_ap=len(lista_apartamente)+1+len(Lista_Apartamente), id_complex=c.id_complex, nr_bloc=bloc+1, nr_etaj=etaj, nr_ap=etaj*100+i+9,
                                                            tip_ap="Aparatamente cu 3 camere", dimensiune=random.randint(70, 90), bloc_vanzare=angajat_fals(bloc+1), statut="free"))
                else:
                    for i in range(2):
                        lista_apartamente.append(Apartament(id_ap=len(lista_apartamente)+1+len(Lista_Apartamente), id_complex=c.id_complex, nr_bloc=bloc+1, nr_etaj=etaj, nr_ap=etaj*100+i+1,
                                                            tip_ap="Penthouse", dimensiune=random.randint(100, 150), bloc_vanzare=angajat_fals(bloc+1), statut="free"))
    for a in lista_apartamente:
        Lista_Apartamente.append(a)
        DB.inserare_DB(a)


def creareExtraOpNoi(Lista_ExtraOp: list):
    lista_extraOp = []
    nr_op = int(input("Cate extra optiuni doriti sa inserati?"))
    for i in range(nr_op):
        denumire = input(f"Dati denumirea pentru optiunea cu nr. {i+1}:")
        pret = int(input("Care va fi pretul acestei optiuni:"))
        lista_extraOp.append(extra_optiune(id_op=i+1+len(Lista_ExtraOp), denumire=denumire, pret=pret))
    for e in lista_extraOp:
        Lista_ExtraOp.append(e)
        DB.inserare_DB(e)


def meniu(lista_complexe: list, lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_extraOp: list,
          lista_clienti: list, lista_contracte: list, lista_cont: list) -> None:   
    lista = [lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_clienti, lista_contracte, lista_cont, DB]
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
        submeniu1(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
                  lista_clienti, lista_contracte, lista_cont)
    elif opt == "2":
        submeniu2(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
                  lista_clienti, lista_contracte, lista_cont)
    elif opt == "3":
        submeniu3(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
                  lista_clienti, lista_contracte, lista_cont)
    elif opt == "4":
        submeniu4(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
                  lista_clienti, lista_contracte, lista_cont)
    elif opt == "5":
        iesire()


def submeniu1(lista_complexe: list, lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_extraOp: list,
              lista_clienti: list, lista_contracte: list, lista_cont: list) -> None:
    print("1. Vizualizare apartamente disponibile + efectuare vanzare")
    print("2. Inapoi")

    opt1 = input(">").strip()
    if opt1 == "1":
        vanzare(lista_complexe, lista_apartamente, lista_vanzari, lista_clienti, lista_contracte,lista_extraOp, DB)
        submeniu1(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
                  lista_clienti, lista_contracte, lista_cont)
    elif opt1 == "2":
        meniu(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
              lista_clienti, lista_contracte, lista_cont)


def submeniu2(lista_complexe: list, lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_extraOp: list,
              lista_clienti: list, lista_contracte: list, lista_cont: list) -> None:
    print("1. Vizualizare apartamente disponibile + efectuare inchiriere")
    print("2. Inapoi")

    opt1 = input(">").strip()
    if opt1 == "1":
        inchiriere(lista_complexe, lista_apartamente, lista_inchirieri, lista_clienti, lista_contracte, DB)
        submeniu2(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
                  lista_clienti, lista_contracte, lista_cont)
    elif opt1 == "2":
        meniu(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
              lista_clienti, lista_contracte, lista_cont)


def submeniu3(lista_complexe: list, lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_extraOp: list,
              lista_clienti: list, lista_contracte: list, lista_cont: list) -> None:
    print("1. Vizualizare minim apartamente vandute pentru profit")
    print("2. Vizualizare minim apartamnete vandute pentru un complex nou")
    print("3. Inapoi")

    opt1 = input(">").strip()
    if opt1 == "1":
        Vizualizare_Profit(lista_cont, lista_complexe)
        submeniu3(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
                  lista_clienti, lista_contracte, lista_cont)
    elif opt1 == "2":
        Vizualizare_ComplexNou(lista_cont, lista_complexe)
        submeniu3(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
                  lista_clienti, lista_contracte, lista_cont)
    elif opt1 == "3":
        meniu(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
              lista_clienti, lista_contracte, lista_cont)


def submeniu4(lista_complexe: list, lista_apartamente: list, lista_vanzari: list, lista_inchirieri: list, lista_extraOp: list,
              lista_clienti: list, lista_contracte: list, lista_cont: list) -> None:
    if input("Doriti sa inregistrati un complex nou?").capitalize() == "Da":
        creareComplexeNoi(lista_complexe)
        meniu(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
              lista_clienti, lista_contracte, lista_cont)
    else:
        meniu(lista_complexe, lista_apartamente, lista_vanzari, lista_inchirieri, lista_extraOp,
              lista_clienti, lista_contracte, lista_cont)


def iesire():
    exit()
