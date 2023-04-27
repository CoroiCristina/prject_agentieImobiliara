import threading
from datetime import datetime, timedelta
from .contabilitatea import pierderi


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


def myThread(lista_apartamente, lista_vanzari, lista_inchiriei, lista_pierderi):
    with lock:
        for ap in lista_apartamente:
            contor = 0
            if ap.status != "free":
                for v in lista_vanzari:
                    if v.apartament == ap.id_cod:
                        contor = 1
                if contor == 0:
                    for i in lista_inchiriei:
                        if i.apartament == ap.id_cod:
                            contor = 1
                    if contor == 0:
                        ap.status == "free"
        for i in lista_inchiriei:
            if datetime.strptime(i.data_iesire, '%Y-%m-%d') <= datetime.today():
                for ap in lista_apartamente:
                    if i.apartament == ap.id_cod:
                        ap.status == "free"
        contor = 0
        for p in lista_pierderi:
            if p.data == str(datetime.today().date()):
                contor = 1
        if ultima_zi_lucratoare() and contor != 1:
            contor = 0
            for ap in lista_apartamente:
                if ap.status == "free":
                    contor += 1
            lista_pierderi.append(pierderi(data=str(datetime.today().date()), suma=contor*150/5))
