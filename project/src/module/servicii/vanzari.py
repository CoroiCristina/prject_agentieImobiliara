from datetime import date
from module.oferta.extra_optiuni import alegere_extraOP
from .Bot import negociere


class vanzare:
    def __init__(self, apartament: int, suma_incasata: int, data_vanzare: date = date.today()) -> None:
        self.apartament = apartament
        self.suma_incasata = suma_incasata
        self.data_vanzare = data_vanzare

    def __str__(self) -> str:
        return (f"{self.apartament},{self.suma_incasata},{self.data_vanzare}")


def filtru(lista_apartamente: list) -> None:
    opt = input("Doriti sa aplicati un filtru pentru a putea vedea datele mai usor?")
    if opt.capitalize() == "Da":
        strada = input("Introduceti strada ce va intereseaza:").capitalize()
        for ap in lista_apartamente:
            if ap.strada == strada and ap.blok_vanzare == 1 and ap.status == "free":
                print(str(ap))
    else:
        for ap in lista_apartamente:
            if ap.blok_vanzare == 1:
                print(str(ap))


def Vanzare(lista_apartamente: list, lista_vanzari: list) -> None:
    filtru(lista_apartamente)
    print("Doriti sa efectuati o vanzare?")
    if input(">").capitalize() == "Da":
        id_cod = int(input("Introduceti codul apartamentului ce va fi vandut: "))
        for ap in lista_apartamente:
            if ap.id_cod == id_cod and ap.status == "free" and ap.blok_vanzare == 1:
                apartament = ap
            else:
                apartament = None
        if apartament is not None:
            pret_apartament = apartament.marime*1500  # euro mp
            if pret_apartament > 80000:
                print("Imobilul are deja un potential cumparator, se vor efectua negocieri intre clienti")
                pret_apartament = negociere(pret_apartament, apartament)
                if pret_apartament != 0:
                    pret_extra = alegere_extraOP()
                    inregistrarevanzare(apartament, pret_apartament, lista_vanzari, pret_extra)
                else:
                    print("Apartamentul nu va mai fi vandut")
            else:
                print(f"Pretul apartamentului este de {pret_apartament}")
                pret_extra = alegere_extraOP()
                inregistrarevanzare(ap, pret_apartament, lista_vanzari)
        else:
            print("Apartament indisponibil!")


def inregistrarevanzare(apartament: object, pret_apartament: list, lista_vanzari: list, pret_extra: int) -> None:
    pret_final = pret_apartament + pret_extra
    print("Pretul final este ", pret_final, " euro")
    obj = vanzare(apartament.id_cod, pret_final)
    apartament.status = "Vandut"
    lista_vanzari.append(obj)
    print("Date inregistrate cu succes!")
