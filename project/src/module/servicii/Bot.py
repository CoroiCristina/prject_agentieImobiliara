import threading
import random
import time

# Crearea unui obiect Lock pentru a evita conflictul între thread-uri
lock = threading.Lock()
# Definirea funcției de negociere


def negociere(pret_apartament: int, apartament: object) -> int:
    # Simularea unei negociere între cei doi clienți: client1=bot sau client fals
    print("Începerea negocierii între client1 și client2...")
    # Ocuparea obiectului Lock pentru a evita conflictul între thread-uri
    with lock:
        print(f"client1: Am solicitat primul sa cumpar apartamentul {apartament.nr_apartament}!")
        dorinta_client1 = 100
        dorinta_client2 = 100
        suma_negociata1 = 1
        suma_negociata2 = 1
        while dorinta_client1 != 0:
            if dorinta_client2 != 0:
                suma_negociata1 = random.randint(suma_negociata2, suma_negociata2+1000)
                time.sleep(1)
                print("oferta client1: ", suma_negociata1)
                suma_negociata2 = random.randint(suma_negociata1, suma_negociata1+1000)
                time.sleep(1)
                print("oferta client2: ", suma_negociata2)
                dorinta_client1 = random.randint(0, dorinta_client1)
                time.sleep(1)
                print("Dorinta clientului1 a scazut la ", dorinta_client1, "%")
                dorinta_client2 = random.randint(0, dorinta_client2)
                time.sleep(1)
                print("Dorinta clientului2 a scazut la ", dorinta_client2, "%")
            else:
                dorinta_client1 = 0
        if dorinta_client2 != 0:
            pret_apartament = pret_apartament+suma_negociata2
            return pret_apartament
        else:
            return 0
