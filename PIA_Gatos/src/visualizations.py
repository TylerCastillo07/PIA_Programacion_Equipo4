import matplotlib.pyplot as plt
import os

def configurar_carpeta_plots():
    """Crea la carpeta específica solicitada por la rúbrica."""
    ruta = os.path.join("results", "plots")
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    return ruta

def graficar_histograma_inteligencia(datos):
    try:
        folder = configurar_carpeta_plots()
        datos_filtrados = [d for d in datos if d > 0]
        plt.figure(figsize=(8, 5))
        plt.hist(datos_filtrados, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5], 
                 rwidth=0.8, color='skyblue', edgecolor='black')
        plt.title("Distribución de Inteligencia (Razas de Gatos)")
        plt.xlabel("Nivel de Inteligencia")
        plt.ylabel("Frecuencia")
        plt.xticks([1, 2, 3, 4, 5])
        
        # Guardado en la ruta correcta
        plt.savefig(os.path.join(folder, "histograma_inteligencia.png"))
        plt.close()
    except Exception as e: print(f"Error Histograma: {e}")

def graficar_barras_energia(nombres, energias):
    try:
        folder = configurar_carpeta_plots()
        top = sorted(zip(nombres, energias), key=lambda x: x[1], reverse=True)[:10]
        n, e = zip(*top)
        plt.figure(figsize=(10, 6))
        plt.bar(n, e, color='orange')
        plt.title("Top 10 Razas con Más Energía")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Guardado en la ruta correcta
        plt.savefig(os.path.join(folder, "barras_energia.png"))
        plt.close()
    except Exception as e: print(f"Error Barras: {e}")

def graficar_dispersion_peso_inteligencia(pesos, inteligencias):
    try:
        folder = configurar_carpeta_plots()
        plt.figure(figsize=(8, 5))
        plt.scatter(pesos, inteligencias, color='purple', alpha=0.5)
        plt.title("Relación Peso vs Inteligencia")
        plt.xlabel("Peso (kg)")
        plt.ylabel("Inteligencia")
        
        # Guardado en la ruta correcta
        plt.savefig(os.path.join(folder, "dispersion_peso_inteligencia.png"))
        plt.close()
    except Exception as e: print(f"Error Dispersión: {e}")

def graficar_pastel_adaptabilidad(datos):
    try:
        folder = configurar_carpeta_plots()
        niveles = [datos.count(i) for i in range(1, 6)]
        labels = ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4', 'Nivel 5']
        plt.figure(figsize=(8, 8))
        plt.pie(niveles, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Proporción de Adaptabilidad")
        
        # Guardado en la ruta correcta
        plt.savefig(os.path.join(folder, "pastel_adaptabilidad.png"))
        plt.close()
    except Exception as e: print(f"Error Pastel: {e}")
