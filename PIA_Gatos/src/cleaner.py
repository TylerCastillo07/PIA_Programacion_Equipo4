import re

def limpiar_datos(data):
    
    peso_texto = data.get("weight", {}).get("metric", "0")
    numeros = re.findall(r"\d+", peso_texto)
    peso_final = int(numeros[0]) if numeros else 0

    
    clean = {
        "id": data.get("id"),
        "raza": data.get("name", "").capitalize(),
        "origen": data.get("origin", "Desconocido"),
        "inteligencia": int(data.get("intelligence", 0)),
        "energia": int(data.get("energy_level", 0)),
        "peso_min_kg": peso_final
    }
    return clean
