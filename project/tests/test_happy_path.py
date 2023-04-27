from src.module.oferta.tipApartament import Garsoniera
from src.module.servicii.vanzari import inregistrarevanzare
from src.module.servicii.inchirieri import inregistrareInchiriere


def test_efectuareVanzare():
    lista_v = []
    garsoniera_noua = Garsoniera(id_cod=1, denumire_complex="Sf.Maria",
                                 strada="Posta Veche", bloc=1,
                                 etaj=0, nr_apartament=1, status="free")
    pret_extra = 0
    inregistrarevanzare(garsoniera_noua, garsoniera_noua.marime*1500, lista_v, pret_extra)
    assert len(lista_v) == 1


def test_efectuare_inchiriere():
    apartament = Garsoniera(id_cod=1, denumire_complex="Sf.Maria",
                            strada="Posta Veche", bloc=1,
                            etaj=0, nr_apartament=1, status="free")
    lista_inchiriere = []
    nr_persoane = 3
    data_intrare = "2022-02-01"
    data_iesire = "2023-02-01"
    inregistrareInchiriere(lista_inchiriere, apartament, nr_persoane, data_intrare, data_iesire)
    assert len(lista_inchiriere) == 1
