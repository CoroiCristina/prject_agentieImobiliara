from pydantic import BaseModel


class Complex(BaseModel):
    id_complex: int
    denumire: str
    strada: str
    nr_blocuri: int

if __name__ == "__main__":
    complex = Complex(id_complex=1, denumire="Arcada", strada="Posta Veche", nr_blocuri=3)