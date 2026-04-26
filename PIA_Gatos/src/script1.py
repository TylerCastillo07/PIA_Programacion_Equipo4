import json
import os
from src.api_client import get_data
from src.validators import validar_nombre, validar_id, validar_inteligencia
from src.cleaner import limpiar_datos

def integrar_flujo_script1():
    print("=== INTEGRACIÓN SCRIPT 1 - FCFM ===")
    
    # URL de la API de Gatos
    url = "https://api.thecatapi.com/v1/breeds"
    
    # 1. Conexión a la API 
    print("Conectando a la API...")
    datos_crudos = get_data(url)
    
    if not datos_crudos:
        print("Error: No se pudieron obtener datos de la API.")
        return

    # Asegurar que existan las carpetas para el guardado
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/clean", exist_ok=True)

    # 2. Guardar respaldo 
    ruta_raw = "data/raw/respuesta_cruda.json"
    try:
        with open(ruta_raw, "w") as f_raw:
            json.dump(datos_crudos, f_raw, indent=4)
        print(f"Respaldo crudo guardado en: {ruta_raw}")
    except IOError as e:
        print(f"No se pudo guardar el respaldo crudo: {e}")

    gatos_limpios = []
    registros_validos = 0
    registros_saltados = 0

    print("Iniciando proceso de validación y limpieza...")
    
    # 3. Ciclo de Validación y Limpieza
    for gato in datos_crudos:
        # Extraer valores para validación con Regex
        id_gato = gato.get("id", "")
        nombre_gato = gato.get("name", "")
        inteligencia_gato = gato.get("intelligence", "")

        # Aplicar las 3 validaciones
        if (validar_id(id_gato) and 
            validar_nombre(nombre_gato) and 
            validar_inteligencia(inteligencia_gato)):
            
            # 4. Si es válido, limpiar y normalizar
            gato_procesado = limpiar_datos(gato)
            if gato_procesado:
                gatos_limpios.append(gato_procesado)
                registros_validos += 1
        else:
            registros_saltados += 1

    # 5. Guardado de Datos Limpios Finales
    ruta_clean = "data/clean/datos_limpios.json"
    try:
        with open(ruta_clean, "w") as f_clean:
            json.dump(gatos_limpios, f_clean, indent=4)
        
        print("-" * 30)
        print("¡FLUJO COMPLETADO CON ÉXITO!")
        print(f"Registros procesados y válidos: {registros_validos}")
        print(f"Registros descartados: {registros_saltados}")
        print(f"Archivo final generado en: {ruta_clean}")
        
    except IOError as e:
        print(f"Error al guardar los datos limpios: {e}")

if __name__ == "__main__":
    integrar_flujo_script1()

