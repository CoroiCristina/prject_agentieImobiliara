from pydantic import BaseModel


class Inregistrare(BaseModel):
    cod_inregistrare: int
    data: str
    suma: int
    detalii: str