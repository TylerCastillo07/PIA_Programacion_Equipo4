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
            
        
        nombres = [g.get("nombre") or g.get("name", "N/A") for g in datos]
        inteligencias = [g.get("inteligencia") or g.get("intelligence", 0) for g in datos]
        energias = [g.get("nivel_energia") or g.get("energy_level", 0) for g in datos]
        pesos = [g.get("peso_kg", 0) for g in datos]
        adaptabilidad = [g.get("adaptabilidad") or g.get("social_needs", 3) for g in datos]

        print(f"\n[INFO] Se cargaron {len(datos)} registros de 'datos_limpios.json'")
        
        print("\n--- ESTADÍSTICAS DE INTELIGENCIA ---")
        print("\n" + "="*40)
        print(" ESTADÍSTICAS DE INTELIGENCIA".center(40))
        print("="*40)
        print(f"Media:    {calcular_media(inteligencias):.2f}")
        print(f"Mediana:  {calcular_mediana(inteligencias)}")
        print(f"Rango:    {calcular_rango(inteligencias)}")

        print("\n" + "="*40)
        print(" ESTADÍSTICAS DE PESO (KG)".center(40))
        print("="*40)
        print(f"Media:    {calcular_media(pesos):.2f}")
        print(f"Mediana:  {calcular_mediana(pesos)}")
        print(f"Rango:    {calcular_rango(pesos)}")


        print("\n--- GENERANDO GRÁFICAS EN CARPETA 'figures/' ---")
        
        graficar_histograma_inteligencia(inteligencias)
        graficar_barras_energia(nombres, energias)
        graficar_dispersion_peso_inteligencia(pesos, inteligencias)
        graficar_pastel_adaptabilidad(adaptabilidad)
        
        print("\n[ÉXITO] Cálculos completados y gráficas actualizadas.")

    except FileNotFoundError:
        print(f"\n[ERROR] No se encontró el archivo en: {ruta_json}")
        print("Asegúrate de ejecutar 'main.py' o 'script1.py' primero.")
    except json.JSONDecodeError:
        print("\n[ERROR] El archivo JSON está corrupto o vacío.")
    except Exception as e:
        print(f"\n[ERROR INESPERADO] {e}")

if __name__ == "__main__":
    ejecutar_analisis()
