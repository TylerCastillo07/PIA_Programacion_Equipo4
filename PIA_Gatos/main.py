import json
import os
from src.utils import imprimir_banner
from src.api_client import get_data
from src.validators import validar_nombre, validar_id, validar_inteligencia
from src.cleaner import limpiar_datos

def asegurar_directorios():
    """Crea las carpetas data/raw y data/clean si no existen"""
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/clean", exist_ok=True)

def ejecutar_proyecto():
    imprimir_banner("PROYECTO GATOS - FCFM")
    asegurar_directorios()
    
    url = "https://api.thecatapi.com/v1/breeds"
    
    # 1. Obtener datos
    print("Iniciando conexión con la API...")
    datos_crudos = get_data(url)
    
    if datos_crudos:
        # Guardar respaldo en RAW
        ruta_raw = os.path.join("data", "raw", "respuesta_cruda.json")
        with open(ruta_raw, "w") as f_raw:
            json.dump(datos_crudos, f_raw, indent=4)
        print(f"-> Datos originales guardados en: {ruta_raw}")

        gatos_limpios = []
        saltados = 0
        
        print("Validando y procesando registros...")
        for gato in datos_crudos:
            # Extraer valores para validar
            id_gato = gato.get("id", "")
            nombre_gato = gato.get("name", "")
            intel_gato = gato.get("intelligence", "")

            # Ejecutar las 3 validaciones de Regex
            v_id = validar_id(id_gato)
            v_nom = validar_nombre(nombre_gato)
            v_int = validar_inteligencia(intel_gato)

            if v_id and v_nom and v_int:
                # 3. Limpiar si pasa las validaciones
                gato_procesado = limpiar_datos(gato)
                gatos_limpios.append(gato_procesado)
            else:
                saltados += 1
                # Esto te avisará en la terminal si algún gato no pasó el Regex
        
        # 4. Guardar resultado limpio
        ruta_clean = os.path.join("data", "clean", "datos_limpios.json")
        with open(ruta_clean, "w") as f_clean:
            json.dump(gatos_limpios, f_clean, indent=4)
            
        print("-" * 40)
        print(f"¡Proceso terminado!")
        print(f"Registros válidos: {len(gatos_limpios)}")
        print(f"Registros saltados: {saltados}")
        print(f"Archivo final: {ruta_clean}")

if __name__ == "__main__":
    ejecutar_proyecto()

