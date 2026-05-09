import pandas as pd
import os

def generar_excel(datos, resultados, ruta_salida):
    """
    Genera un archivo Excel con múltiples hojas:
    1. Datos tabulares limpios.
    2. Resumen de estadísticas.
    3. Tablas de frecuencia.
    """
    try:
        # Asegurar que la carpeta exista
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        
        with pd.ExcelWriter(ruta_salida, engine='openpyxl') as writer:
            # HOJA 1: Datos Tabulares Limpios
            df_datos = pd.DataFrame(datos)
            df_datos.to_excel(writer, sheet_name='Datos_Limpios', index=False)
            
            # HOJA 2: Estadísticas (Media, Mediana, Moda, Rango)
            # Transformamos el diccionario de resultados a un formato tabular
            resumen_stats = []
            for var, stats in resultados.items():
                resumen_stats.append({
                    "Variable": var,
                    "Media": stats["media"],
                    "Mediana": stats["mediana"],
                    "Moda": stats["moda"],
                    "Rango": stats["rango"]
                })
            df_stats = pd.DataFrame(resumen_stats)
            df_stats.to_excel(writer, sheet_name='Estadisticas', index=False)
            
            # HOJA 3: Tablas de Frecuencia
            # Creamos una hoja que muestre la frecuencia de cada nivel por variable
            frecuencias_lista = []
            for var, stats in resultados.items():
                for nivel, cuenta in stats["tabla_frecuencia"].items():
                    frecuencias_lista.append({
                        "Variable": var,
                        "Nivel/Valor": nivel,
                        "Frecuencia (Cantidad)": cuenta
                    })
            df_frecuencias = pd.DataFrame(frecuencias_lista)
            df_frecuencias.to_excel(writer, sheet_name='Frecuencias', index=False)
            
        return True
    except Exception as e:
        print(f"Error al generar Excel: {e}")
        return False
