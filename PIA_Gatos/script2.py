import os
import sys
import json
import pandas as pd


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.analysis import (
    calcular_media, calcular_mediana, calcular_rango, 
    calcular_moda, generar_tabla_frecuencia 
)
from src.utils import imprimir_banner
from src.visualizations import (
    graficar_histograma_inteligencia,
    graficar_barras_energia,
    graficar_dispersion_peso_inteligencia,
    graficar_pastel_adaptabilidad
)
from src.datasheet import generar_excel

def ejecutar_analisis():
    imprimir_banner("ANÁLISIS ESTADÍSTICO Y VISUAL - EQUIPO 4")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    ruta_json_datos = os.path.join(base_path, "data", "clean", "datos_limpios.json")
    
    try:
        # 1. Cargar datos limpios
        with open(ruta_json_datos, "r", encoding='utf-8') as f:
            datos = json.load(f)
            
        # 2. Extracción de listas de datos para procesar
        nombres = [g.get("nombre", "N/A") for g in datos]
        inteligencias = [g.get("inteligencia", 0) for g in datos]
        energias = [g.get("nivel_energia", 0) for g in datos]
        pesos = [g.get("peso_kg", 0) for g in datos]
        adaptabilidades = [g.get("adaptabilidad", 0) for g in datos]

        # 3. Cálculo de Estadísticas (Requisito: 5 cálculos por variable)
        resultados = {
            "inteligencia": {
                "media": calcular_media(inteligencias),
                "mediana": calcular_mediana(inteligencias),
                "moda": calcular_moda(inteligencias),
                "rango": calcular_rango(inteligencias),
                "tabla_frecuencia": generar_tabla_frecuencia(inteligencias)
            },
            "peso_kg": {
                "media": calcular_media(pesos),
                "mediana": calcular_mediana(pesos),
                "moda": calcular_moda(pesos),
                "rango": calcular_rango(pesos),
                "tabla_frecuencia": generar_tabla_frecuencia(pesos)
            },
            "nivel_energia": {
                "media": calcular_media(energias),
                "mediana": calcular_mediana(energias),
                "moda": calcular_moda(energias),
                "rango": calcular_rango(energias),
                "tabla_frecuencia": generar_tabla_frecuencia(energias)
            },
            "adaptabilidad": {
                "media": calcular_media(adaptabilidades),
                "mediana": calcular_mediana(adaptabilidades),
                "moda": calcular_moda(adaptabilidades),
                "rango": calcular_rango(adaptabilidades),
                "tabla_frecuencia": generar_tabla_frecuencia(adaptabilidades)
            }
        }

        
        os.makedirs("results", exist_ok=True)
        ruta_stats_json = os.path.join("results", "statistics.json")
        with open(ruta_stats_json, "w", encoding='utf-8') as f_res:
            json.dump(resultados, f_res, indent=4, ensure_ascii=False)

        print(f"\n[INFO] Reporte JSON generado en: {ruta_stats_json}")

        
        ruta_excel = os.path.join(base_path, "results", "excel", "Analisis_Felino_Equipo4.xlsx")
        print("--- GENERANDO ARCHIVO EXCEL ---")
        if generar_excel(datos, resultados, ruta_excel):
            print(f"[ÉXITO] Archivo Excel creado en: {ruta_excel}")
        
        
        print("\n--- ACTUALIZANDO VISUALIZACIONES ---")
        graficar_histograma_inteligencia(inteligencias)
        graficar_barras_energia(nombres, energias)
        graficar_dispersion_peso_inteligencia(pesos, inteligencias)
        graficar_pastel_adaptabilidad(adaptabilidades)
        
        
        print("\n" + "="*40)
        print(" RESUMEN FINAL ".center(40, "="))
        for llave in resultados:
            print(f"> {llave.upper()}: Media={resultados[llave]['media']:.2f}, Moda={resultados[llave]['moda']}")
        print("="*40)
        print("\n[ÉXITO] Proceso del Script 2 completado sin errores.")

    except Exception as e:
        print(f"\n[ERROR INESPERADO] {e}")

if __name__ == "__main__":
    ejecutar_analisis()
