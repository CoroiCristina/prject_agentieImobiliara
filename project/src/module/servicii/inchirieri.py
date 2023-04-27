from datetime import datetime


class inchiriere:
    def __init__(self, data_intrare: str, data_iesire: str, apartament: int, nr_persoane: int) -> None:
        self.data_intrare = data_intrare
        self.data_iesire = data_iesire
        self.data_aux = data_intrare
        self.apartament = apartament
        self.nr_persoane = nr_persoane
        self.pret_luna = self.stabilirePret_luna()
        self.perioada = self.perioada_de_timp(data_intrare, data_iesire)
        self.bani_incasati = self.incasare_chirie()

    def __str__(self) -> str:
        return (f"{self.data_intrare},{self.data_iesire},{self.apartament},{self.nr_persoane}")

    def stabilirePret_luna(self) -> int:
        if self.nr_persoane == 1:
            pret = 100/5  # Curs euro
            return pret
        elif self.nr_persoane == 2:
            pret = 200/5
            return pret
        elif self.nr_persoane == 3 or self.nr_persoane == 4:
            pret = 350/5
            return pret
        elif self.nr_persoane >= 5:
            pret = 600/5
            return pret

    def perioada_de_timp(self, data_intrare: str, data_iesire: str) -> int:
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
        perioada = self.perioada_de_timp(self.data_aux, str(datetime.today().date()))
        bani_incasati = perioada*self.pret_luna
        return bani_incasati
        # Aceasta functie ar trebui facuta ca un proces aparte care sa verifice in fiecare zi de plata a lunii daca au intrat
        # banii in contul agentiei, iar daca nu sa trimita o avertizare chiriasului si agentiei


def filtruInchirieri(lista_apartamente: list):
    opt = input("Doriti sa aplicati un filtru pentru a putea vedea datele mai usor?")
    if opt.capitalize() == "Da":
        strada = input("Introduceti strada ce va intereseaza:").capitalize()
        for ap in lista_apartamente:
            if ap.strada == strada and ap.blok_vanzare == 0 and ap.status == "free":
                print(str(ap))
    else:
        for ap in lista_apartamente:
            if ap.blok_vanzare == 0 and ap.status == "free":
                print(str(ap))


def Inchiriere(lista_apartamente, lista_inchirieri):
    filtruInchirieri(lista_apartamente)
    if input("Doriti sa inregistrati o inchiriere?").capitalize() == "Da":
        id_cod = int(input("Introduceti ID-ul apartamentului ce va fi inchiriat:"))
        nr_persoane = int(input("Introduceti numarul de persoane:"))
        data_intrare = input("introduceti data de intrare a locatarilor (format %Y-%m-%d):")
        data_iesire = input("Introduceti data de iesire a locatarilor(format %Y-%m-%d):")
        for ap in lista_apartamente:
            if ap.id_cod == id_cod and ap.blok_vanzare != 1 and ap.status == "free":
                apartament = ap
            else:
                apartament = None
                print("Apartament indisponibil!")
        if apartament is not None:
            inregistrareInchiriere(lista_inchirieri, apartament, nr_persoane, data_intrare, data_iesire)


def inregistrareInchiriere( lista_inchirieri, apartament, nr_persoane, data_intrare, data_iesire):
    lista_inchirieri.append(inchiriere(data_intrare, data_iesire, apartament.id_cod, nr_persoane))
    apartament.status = "Inchiriat"
    print("Date inregistrate cu succes!")
