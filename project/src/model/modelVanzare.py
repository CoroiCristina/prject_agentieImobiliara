from pydantic import BaseModel
from typing import Optional


class Vanzare(BaseModel):
    nr_contract: Optional[int]
    data: str
    suma: int
    cod_v: int
