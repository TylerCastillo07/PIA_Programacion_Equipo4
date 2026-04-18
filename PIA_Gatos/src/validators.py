import re

def validar_id(id_valor):
    # El ID siempre son 4 letras minúsculas
    return bool(re.search(r"^[a-z]{4}$", str(id_valor)))

def validar_nombre(nombre):
    # Agregamos "-" para nombres como "American-Bobtail"
    return bool(re.search(r"^[A-Za-z\s\-]+$", str(nombre)))

def validar_inteligencia(valor):
    #Aseguramos que sea 1-5
    return bool(re.search(r"^[1-5]$", str(valor)))

