import threading
from datetime import datetime, timedelta
from .contabilitatea import Inregistrare_contBancar
from module.oferta.apartamente import Apartament


def ultima_zi_lucratoare():
    today = datetime.today().date()

    if today.weekday() == 4:   # verifica daca ziua curenta este vineri
        next_day = today + timedelta(days=1)  # determina urmatoarea zi
        if next_day.month != today.month + 1:   # verifica daca urmatoarea zi este prima zi lucratoare a lunii urmatoare
            return True
    elif today.weekday() == 5:   # verifica daca ziua curenta este sambata
        next_day = today + timedelta(days=2)   # determina urmatoarea zi
        if next_day.month != today.month + 1:   # verifica daca urmatoarea zi este prima zi lucratoare a lunii urmatoare
            return True
    else:
        return False


lock = threading.Lock()


def myThread(*lista):
    print(len(lista[5]))
    with lock:
        for c in lista[5]:
            contor = 0
            ok = 0
            for ap in lista[1]:
                if ap.statut != "free":
                    if c.id_ap == ap.id_ap:
                        for v in lista[2]:
                            if v.nr_contract == c.nr_contract:
                                ok = 0
                                for inr in lista[6]:
                                    if inr.detalii == f"Vanzare apartament{ap.id_ap}":
                                        ok = 1
                                if ok != 1:
                                    lista[6].append(Inregistrare_contBancar(cod_inregistrare=len(lista[6])+1, data=str(datetime.today()), suma=v.suma, detalii=f"Vanzare apartament{ap.id_ap}"))
                                    lista[7].inserare_DB(lista[6][-1])
                                    contor = 1
                        if contor == 0:
                            for i in lista[3]:
                                if i.nr_contract == c.nr_contract:
                                    ok = 0
                                    for inr in lista[6]:
                                        if inr.detalii == f"Inchiriere apartament{ap.id_ap}":
                                            ok = 1
                                    if ok != 1 and int(i.zi_plata) == int(datetime.today().day()) and datetime.strptime(i.data_iesire, '%Y-%m-%d') <= datetime.today():
                                        lista[6].append(Inregistrare_contBancar(cod_inregistrare=len(lista[6])+1, data=str(datetime.today()), suma=i.suma_chirie, detalii=f"Inchiriere apartament{ap.id_ap}"))
                                        lista[7].inserare_DB(lista[6][-1])
                                        contor = 1
            if contor == 0:
                lista[5].remove(c)
                lista[7].DeleteDB(c.nr_contract)
                ap.statut == "free"
                lista[7].update_ApartamentDB(Apartament, ap.id_ap, ap.statut)
        for i in lista[3]:
            if datetime.strptime(i.data_iesire, '%Y-%m-%d') <= datetime.today():
                for ap in lista[1]:
                    if i.id_ap == ap.id_ap:
                        ap.statut == "free"
        contor = 0
        for p in lista[6]:
            if p.data == str(datetime.today().date()):
                contor = 1
        if ultima_zi_lucratoare() and contor != 1:
            contor = 0
            for ap in lista[1]:
                if ap.statut == "free":
                    contor += 1
            lista[6].append(Inregistrare_contBancar(cod_inregistrare=len(lista[6])+1), data=str(datetime.today()), suma=-contor*150, detelii="Pierderi Administrative")
            lista[7].inserare_DB(lista[6][-1])
