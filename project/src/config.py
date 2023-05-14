from module.oferta.dataBaseAcces import DBAccess

STORAGE = DBAccess()

def get_storage():
    return STORAGE