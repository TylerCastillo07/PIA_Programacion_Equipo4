import json
import os
import sys
from api_client import get_data
from cleaner import limpiar_datos
from validators import validar_nombre, validar_id, validar_inteligencia

def integrar_flujo_script1():
    print("=== INTEGRACIÓN SCRIPT 1 - FCFM (REVISADO) ===")
    
    # 1. Configuración de rutas (Subiendo un nivel desde 'src' a la raíz)
    # Esto asegura que se cree 'data/' en la raíz del proyecto y no dentro de 'src'
    src_path = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(os.path.join(src_path, '..'))
    
    ruta_raw = os.path.join(base_path, "data", "raw", "respuesta_cruda.json")
    ruta_clean = os.path.join(base_path, "data", "clean", "datos_limpios.json")
    
    # Asegurar que existan las carpetas en la raíz
    os.makedirs(os.path.dirname(ruta_raw), exist_ok=True)
    os.makedirs(os.path.dirname(ruta_clean), exist_ok=True)

    # 2. Conexión a la API
    url = "https://api.thecatapi.com/v1/breeds"
    print("Conectando a la API...")
    datos_crudos = get_data(url)
    
    if not datos_crudos:
        print("[ERROR] No se pudieron obtener datos de la API.")
        return

    # 3. Guardar respaldo crudo
    try:
        with open(ruta_raw, "w", encoding='utf-8') as f_raw:
            json.dump(datos_crudos, f_raw, indent=4, ensure_ascii=False)
        print(f"[OK] Respaldo crudo guardado en: {ruta_raw}")
    except IOError as e:
        print(f"[ERROR] No se pudo guardar el respaldo: {e}")

    # 4. Ciclo de Validación y Limpieza
    gatos_limpios = []
    registros_validos = 0
    registros_saltados = 0

    print("Iniciando proceso de validación y limpieza...")
    
    for gato in datos_crudos:
        # Extraer valores para validación
        id_val = gato.get("id", "")
        nombre_val = gato.get("name", "")
        intel_val = gato.get("intelligence", "")

        # Validaciones con Regex y Lógica
        if (validar_id(id_val) and 
            validar_nombre(nombre_val) and 
            validar_inteligencia(intel_val)):
            
            gato_procesado = limpiar_datos(gato)
            if gato_procesado:
                gatos_limpios.append(gato_procesado)
                registros_validos += 1
        else:
            registros_saltados += 1

    
    print(f"DEBUG: Cantidad de registros que pasaron los filtros: {len(gatos_limpios)}")

    # 5. Guardado de Datos Limpios Finales (Escritura Segura)
    if registros_validos > 0:
        try:
            with open(ruta_clean, "w", encoding='utf-8') as f_clean:
                json.dump(gatos_limpios, f_clean, indent=4, ensure_ascii=False)
                f_clean.flush()
                os.fsync(f_clean.fileno())
            
            print("-" * 30)
            print("¡FLUJO COMPLETADO CON ÉXITO!")
            print(f"Registros válidos: {registros_validos}")
            print(f"Registros descartados: {registros_saltados}")
            print(f"Archivo final generado en: {ruta_clean}")
            
        except IOError as e:
            print(f"[ERROR CRÍTICO] No se pudo escribir el archivo final: {e}")
    else:
        print("[ADVERTENCIA] No hubo registros válidos para guardar. Revisa tus validadores.")

if __name__ == "__main__":
    integrar_flujo_script1()

