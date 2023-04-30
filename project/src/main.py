from UI.utility import (meniu,
                        citire_fisier,
                        creareOferta)
print("MODIFICAT")

if __name__ == "__main__":
    print("hello!")
    lista_apartamente = []
    lista_vanzari = []
    lista_inchirieri = []
    lista_pierderi = []
    with open("oferta.json") as file:
        if not file.read():
            print("Pentru a putea prelucra date va trebui sa inserati intai oferta!!")
            creareOferta(lista_apartamente)
        else:
            citire_fisier(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
    meniu(lista_apartamente, lista_vanzari, lista_inchirieri, lista_pierderi)
