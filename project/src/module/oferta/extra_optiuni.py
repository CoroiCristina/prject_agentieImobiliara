extra_optiuni = {"Minim mobilat": 1000,
                 "Mobilat complet": 5000,
                 "Mobilat Complet+lux": 10000,
                 "Pass": 0}


def alegere_extraOP():
    print("Introduceti extra-optiunea aleasa de catre client:")
    for key in extra_optiuni.keys():
        print(key)
    extra_optiune = input(">").capitalize()
    for key in extra_optiuni.keys():
        if key == extra_optiune:
            return extra_optiune[key]
