from pydantic import BaseModel
from typing import Optional


class Apartament(BaseModel):
    id_ap: int
    id_complex: Optional[int]
    nr_bloc: int
    nr_etaj: int
    nr_ap: int
    tip_ap: str
    dimensiune: int
    bloc_vanzare: int
    statut: str
