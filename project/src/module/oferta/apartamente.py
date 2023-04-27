class apartament:
    def __init__(self, id_cod: int, denumire_complex: str, strada: str, bloc: int, etaj: int, nr_apartament: int, status: str = "free") -> None:
        self.id_cod = id_cod
        self.denumire_complex = denumire_complex
        self.strada = strada
        self.bloc = bloc
        self.etaj = etaj
        self.nr_apartament = nr_apartament
        self.status = status
        self.blok_vanzare = self.angajat_fals()

    def angajat_fals(self) -> int:
        global bloc_vanzare
        if self.bloc != 1:
            bloc_vanzare = 0
        else:
            bloc_vanzare = 1
        return bloc_vanzare
