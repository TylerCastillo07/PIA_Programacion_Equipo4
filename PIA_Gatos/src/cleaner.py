import re

def limpiar_datos(data):
    # Manejo de nulos: si no existe el campo, ponemos un valor por defecto
    nombre = data.get("name", "Desconocido").capitalize()
    
    # Aplanamiento y extracción de peso
    peso_raw = data.get("weight", {}).get("metric", "0")
    numeros = re.findall(r"\d+", peso_raw)
    peso_min = int(numeros[0]) if numeros else 0

    
    return {
        "id": data.get("id", "n/a"),
        "raza": nombre,
        "origen": data.get("origin", "Desconocido"),
        "inteligencia": int(data.get("intelligence", 0)),
        "energia": int(data.get("energy_level", 0)),
        "peso_min_kg": peso_min
    }

