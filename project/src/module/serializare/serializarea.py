import json
from module.oferta.tipApartament import (Garsoniera,
                                         Apartament2Camere,
                                         Apartament3Camere,
                                         Penthouse)
from module.servicii.vanzari import (vanzare)
from module.servicii.inchirieri import inchiriere


class MyEncouder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Garsoniera | Apartament2Camere | Apartament3Camere | Penthouse):
            return o.id_cod, o.denumire_complex, o.strada, o.bloc, o.etaj, o.nr_apartament, o.status, o.marime, o.tip
        elif isinstance(o, vanzare):
            return o.apartament, o.suma_incasata, o.data_vanzare
        elif isinstance(o, inchiriere):
            return o.data_intrare, o.data_iesire, o.apartament, o.nr_persoane
