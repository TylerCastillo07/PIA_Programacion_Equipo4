import json
from src.utils import imprimir_banner
from src.api_client import get_data
from src.validators import validar_nombre, validar_id
from src.cleaner import limpiar_datos

def ejecutar_proyecto():
    imprimir_banner("PROYECTO GATOS - FCFM")
    url = "https://api.thecatapi.com/v1/breeds"
    
    datos_crudos = get_data(url)
    
    if datos_crudos:
        with open("data/raw/respuesta.json", "w") as f_raw:
            json.dump(datos_crudos, f_raw, indent=4)
        print("Archivo 'respuesta.json' guardado en data/raw/")
    

        gatos_limpios = []
        
        for gato in datos_crudos:
            if validar_nombre(gato.get("name", "")) and validar_id(gato.get("id", "")):
                gato_procesado = limpiar_datos(gato)
                gatos_limpios.append(gato_procesado)
        
        with open("data/clean/datos_limpios.json", "w") as f_clean:
            json.dump(gatos_limpios, f_clean, indent=4)
            
        print(f"¡Éxito! Se procesaron {len(gatos_limpios)} razas en data/clean/.")

if __name__ == "__main__":
    ejecutar_proyecto()

