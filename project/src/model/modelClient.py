from pydantic import BaseModel

class Client(BaseModel):
    CNP: str
    nume: str
    prenume: str
    tel: str