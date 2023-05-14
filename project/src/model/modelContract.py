from pydantic import BaseModel
from typing import Optional


class Contract(BaseModel):
    nr_contract: str
    tip_ct: str
    cnp: Optional[str]
    id_ap: Optional[int]
    id_op: Optional[int]