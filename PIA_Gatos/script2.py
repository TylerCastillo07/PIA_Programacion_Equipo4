import os
import sys
import json


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.analysis import calcular_media, calcular_mediana, calcular_rango
from src.utils import imprimir_banner

def ejecutar_analisis():
    imprimir_banner("ANÁLISIS ESTADÍSTICO - EQUIPO 4")
    
    a
    base_path = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(base_path, "data", "clean", "datos_limpios.json")
    
    try:
        with open(ruta_json, "r", encoding='utf-8') as f:
            datos = json.load(f)
            
        
        inteligencias = [g.get("inteligencia", 0) for g in datos]
        niveles_energia = [g.get("nivel_energia", 0) for g in datos]
        pesos = [g.get("peso_kg", 0) for g in datos]

        print(f"\n[INFO] Se cargaron {len(datos)} registros de 'datos_limpios.json'")
        
        print("\n--- ESTADÍSTICAS DE INTELIGENCIA ---")
        print(f"Media:   {calcular_media(inteligencias):.2f}")
        print(f"Mediana: {calcular_mediana(inteligencias)}")
        print(f"Rango:   {calcular_rango(inteligencias)}")

        print("\n--- ESTADÍSTICAS DE PESO (KG) ---")
        print(f"Media:   {calcular_media(pesos):.2f}")
        print(f"Mediana: {calcular_mediana(pesos)}")
        print(f"Rango:   {calcular_rango(pesos)}")

    except FileNotFoundError:
        print(f"\n[ERROR] No se encontró el archivo en: {ruta_json}")
        print("Asegúrate de ejecutar 'main.py' o 'script1.py' primero.")
    except json.JSONDecodeError:
        print("\n[ERROR] El archivo JSON está corrupto o vacío.")
    except Exception as e:
        print(f"\n[ERROR INESPERADO] {e}")

if __name__ == "__main__":
    ejecutar_analisis()
