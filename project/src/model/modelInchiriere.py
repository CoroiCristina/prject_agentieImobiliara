from pydantic import BaseModel
from typing import Optional


class Inciriere(BaseModel):
    cod_in: int
    nr_contract: Optional[int]
    data_intrare: str
    data_iesire: str
    nr_persoane: int
    suna_chirie: int
    nr_plati_ramase: int
    zi_plata: str
