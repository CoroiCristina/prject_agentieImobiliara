import random
from .apartamente import apartament


class Garsoniera(apartament):
    def __init__(self, id_cod: int, denumire_complex: str, strada: str, bloc: int, etaj: int, nr_apartament: int,  status: str, marime: int = random.randint(20, 25), tip: str = "Garsoniera") -> None:
        super().__init__(id_cod, denumire_complex, strada, bloc, etaj, nr_apartament, status)
        self.bloK_vanzare = self.angajat_fals()
        self.marime = marime
        self.tip = tip

    def __str__(self) -> str:
        return (f"ID apartamente: {self.id_cod}, Denumire complex:{self.denumire_complex}, Strada: {self.strada}, Nr_bloc: {self.bloc}, Nr_etaj:{self.etaj}, Nr_apartament: {self.nr_apartament}, Marime: {self.marime}, Tip:{self.tip}")   


class Apartament2Camere(apartament):
    def __init__(self, id_cod: int, denumire_complex: str, strada: str, nr_bloc: int, nr_etaj: int, nr_apartament: int, status: str, marime: int = random.randint(40, 60), tip: str = "Apartament cu 2 camere") -> None:
        super().__init__(id_cod, denumire_complex, strada, nr_bloc, nr_etaj, nr_apartament,  status)
        self.blok_vanzare = self.angajat_fals()
        self.marime = marime
        self.tip = tip

    def __str__(self) -> str:
        return (f"ID apartamente: {self.id_cod}, Denumire complex:{self.denumire_complex}, Strada: {self.strada}, Nr_bloc: {self.bloc}, Nr_etaj:{self.etaj}, Nr_apartament: {self.nr_apartament}, Marime: {self.marime}, Tip:{self.tip}")


class Apartament3Camere(apartament):
    def __init__(self, id_cod: int, denumire_complex: str, strada: str, nr_bloc: int, nr_etaj: int, nr_apartament: int, status: str, marime: int = random.randint(70, 90), tip: str = "Apartament cu 3 camere") -> None:
        super().__init__(id_cod, denumire_complex, strada, nr_bloc, nr_etaj, nr_apartament, status)
        self.blok_vanzare = self.angajat_fals()
        self.marime = marime
        self.tip = tip

    def __str__(self) -> str:
        return (f"ID apartamente: {self.id_cod}, Denumire complex:{self.denumire_complex}, Strada: {self.strada}, Nr_bloc: {self.bloc}, Nr_etaj:{self.etaj}, Nr_apartament: {self.nr_apartament}, Marime: {self.marime}, Tip:{self.tip}")


class Penthouse(apartament):
    def __init__(self, id_cod: int, denumire_complex: str, strada: str, nr_bloc: int, nr_etaj: int, nr_apartament: int, status: str, marime: int = random.randint(100, 150), tip: str = "Penthouse") -> None:
        super().__init__(id_cod, denumire_complex, strada, nr_bloc, nr_etaj, nr_apartament,  status)
        self.blok_vanzare = self.angajat_fals()
        self.marime = marime
        self.tip = tip

    def __str__(self) -> str:
        return (f"ID apartamente: {self.id_cod}, Denumire complex:{self.denumire_complex}, Strada: {self.strada}, Nr_bloc: {self.bloc}, Nr_etaj:{self.etaj}, Nr_apartament: {self.nr_apartament}, Marime: {self.marime}, Tip:{self.tip}")
