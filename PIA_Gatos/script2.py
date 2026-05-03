import os
import sys
import json


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.analysis import calcular_media, calcular_mediana, calcular_rango
from src.utils import imprimir_banner
from src.visualizations import (
    graficar_histograma_inteligencia,
    graficar_barras_energia,
    graficar_dispersion_peso_inteligencia,
    graficar_pastel_adaptabilidad
)

def ejecutar_analisis():
    imprimir_banner("ANÁLISIS ESTADÍSTICO - EQUIPO 4")
    
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(base_path, "data", "clean", "datos_limpios.json")
    
    try:
        with open(ruta_json, "r", encoding='utf-8') as f:
            datos = json.load(f)
            
        
        nombres = [g.get("nombre", "N/A") for g in datos]
        inteligencias = [g.get("inteligencia", 0) for g in datos]
        energias = [g.get("nivel_energia", 0) for g in datos]
        pesos = [g.get("peso_kg", 0) for g in datos]
        adaptabilidad = [g.get("adaptabilidad", 0) for g in datos]

        resultados = {
            "inteligencia": {
                "media": calcular_media(inteligencias),
                "mediana": calcular_mediana(inteligencias),
                "moda": calcular_moda(inteligencias),
                "rango": calcular_rango(inteligencias),
                "tabla_frecuencia": generar_tabla_frecuencia(inteligencias)
            }
        }
        
        os.makedirs("results", exist_ok=True)
        ruta_stats = os.path.join("results", "statistics.json")
        with open(ruta_stats, "w", encoding='utf-8') as f_res:
            json.dump(resultados, f_res, indent=4, ensure_ascii=False)

        print(f"\n[INFO] Reporte generado en: {ruta_stats}")
        print(f"Moda detectada: {resultados['inteligencia']['moda']}")

        # Gráficas
        print("\n--- ACTUALIZANDO VISUALIZACIONES ---")
        
        graficar_histograma_inteligencia(inteligencias)
        graficar_barras_energia(nombres, energias)
        graficar_dispersion_peso_inteligencia(pesos, inteligencias)
        graficar_pastel_adaptabilidad(adaptabilidad)
        
        print("\n[ÉXITO] Proceso completado sin errores.")

    except FileNotFoundError:
        print(f"\n[ERROR] No se encontró el archivo en: {ruta_json}")
        print("Asegúrate de ejecutar 'main.py' o 'script1.py' primero.")
    except json.JSONDecodeError:
        print("\n[ERROR] El archivo JSON está corrupto o vacío.")
    except Exception as e:
        print(f"\n[ERROR INESPERADO] {e}")

if __name__ == "__main__":
    ejecutar_analisis()
