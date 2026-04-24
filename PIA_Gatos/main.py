import json
import os
from src.api_client import get_data
from src.cleaner import limpiar_datos
from src.validators import validar_nombre, validar_id, validar_inteligencia

def ejecutar_proyecto():
    print("=== PROYECTO GATOS FCFM (ROBUSTEZ) ===")
    url = "https://api.thecatapi.com/v1/breeds"
    
    
    datos_crudos = get_data(url)
    
    if not datos_crudos:
        print("No se pudieron obtener datos. Abortando ejecución.")
        return

    gatos_procesados = []
    
   
    for item in datos_crudos:
        try: 
            if (validar_id(item.get("id", "")) and 
                validar_nombre(item.get("name", "")) and 
                validar_inteligencia(item.get("intelligence", ""))):
                
                limpio = limpiar_datos(item)
                if limpio:
                    gatos_procesados.append(limpio)
        except Exception as e:
            print(f"Error crítico en el bucle de procesamiento: {e}")

    
    try:
        os.makedirs("data/clean", exist_ok=True)
        with open("data/clean/datos_limpios.json", "w") as f:
            json.dump(gatos_procesados, f, indent=4)
        print(f"Éxito: Se procesaron {len(gatos_procesados)} registros correctamente.")
    except IOError as e:
        print(f"Error al escribir el archivo en disco: {e}")

if __name__ == "__main__":
    ejecutar_proyecto()

