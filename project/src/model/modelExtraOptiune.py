from pydantic import BaseModel


class ExtraOp(BaseModel):
    id_op: int
    denumire: str
    pret: int