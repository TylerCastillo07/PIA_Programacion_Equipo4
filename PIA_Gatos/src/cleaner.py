import re

def limpiar_datos(gato):
    try:
        
        peso_crudo = gato.get("weight", {}).get("metric", "0")
        numeros = re.findall(r'\d+', peso_crudo)
        
        try:
            peso_kg = int(numeros[0]) if numeros else 0
        except (ValueError, IndexError):
            peso_kg = 0

        
        datos_limpios = {
            "id": gato.get("id", "N/A"),
            "nombre": gato.get("name", "Sin nombre").strip().capitalize(),
            "inteligencia": int(gato.get("intelligence", 0)),
            "peso_kg": peso_kg,
            "origen": gato.get("origin", "Desconocido")
        }
        return datos_limpios
    except Exception as e:
        print(f"Error procesando el gato {gato.get('name')}: {e}")
        return None

