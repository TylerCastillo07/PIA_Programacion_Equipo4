import matplotlib.pyplot as plt
import os

def configurar_carpeta_figures():
    if not os.path.exists("figures"):
        os.makedirs("figures")

def graficar_histograma_inteligencia(datos):
    try:
        configurar_carpeta_figures()
        # Filtramos ceros para que no afecten la gráfica
        datos_filtrados = [d for d in datos if d > 0]
        plt.figure(figsize=(8, 5))
        # Centramos las barras en 1, 2, 3, 4, 5
        plt.hist(datos_filtrados, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5], 
                 rwidth=0.8, color='skyblue', edgecolor='black')
        plt.title("Distribución de Inteligencia (Razas de Gatos)")
        plt.xlabel("Nivel de Inteligencia")
        plt.ylabel("Frecuencia")
        plt.xticks([1, 2, 3, 4, 5])
        plt.savefig("figures/histograma_inteligencia.png")
        plt.close()
    except Exception as e: print(f"Error Histograma: {e}")

def graficar_barras_energia(nombres, energias):
    try:
        configurar_carpeta_figures()
        # Ordenamos para mostrar los 10 más energéticos
        top = sorted(zip(nombres, energias), key=lambda x: x[1], reverse=True)[:10]
        n, e = zip(*top)
        plt.figure(figsize=(10, 6))
        plt.bar(n, e, color='orange')
        plt.title("Top 10 Razas con Más Energía")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig("figures/barras_energia.png")
        plt.close()
    except Exception as e: print(f"Error Barras: {e}")

def graficar_dispersion_peso_inteligencia(pesos, inteligencias):
    try:
        configurar_carpeta_figures()
        plt.figure(figsize=(8, 5))
        plt.scatter(pesos, inteligencias, color='purple', alpha=0.5)
        plt.title("Relación Peso vs Inteligencia")
        plt.xlabel("Peso (kg)")
        plt.ylabel("Inteligencia")
        plt.savefig("figures/dispersion_peso_inteligencia.png")
        plt.close()
    except Exception as e: print(f"Error Dispersión: {e}")

def graficar_pastel_adaptabilidad(datos):
    try:
        configurar_carpeta_figures()
        # Contamos cuántos gatos hay en cada nivel
        niveles = [datos.count(i) for i in range(1, 6)]
        labels = ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4', 'Nivel 5']
        plt.figure(figsize=(8, 8))
        plt.pie(niveles, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Proporción de Adaptabilidad")
        plt.savefig("figures/pastel_adaptabilidad.png")
        plt.close()
    except Exception as e: print(f"Error Pastel: {e}")
