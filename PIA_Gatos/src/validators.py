import re

def validar_nombre(nombre):
    return bool(re.search(r"^[A-Za-z\s]+$", nombre))

def validar_id(id_valor):
    return len(str(id_valor)) == 4
