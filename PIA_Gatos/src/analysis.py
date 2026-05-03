import statistics as stats
from collections import Counter

def calcular_media(lista):
    """Calcula el promedio aritmético atrapando errores de lista vacía."""
    try:
        return stats.mean(lista)
    except stats.StatisticsError:
        return 0

def calcular_mediana(lista):
    """Calcula el valor central de los datos."""
    try:
        return stats.median(lista)
    except stats.StatisticsError:
        return 0

def calcular_rango(lista):
    """Calcula la diferencia entre el valor máximo y mínimo."""
    if not lista:
        return 0
    return max(lista) - min(lista)

def calcular_moda(lista):
    """Calcula el valor que más se repite."""
    if not lista: return 0
    try:
        return stats.mode(lista)
    except stats.StatisticsError:
        return stats.multimode(lista)[0]

def generar_tabla_frecuencia(lista):
    """Cuenta cuántos elementos hay de cada tipo."""
    return dict(Counter(lista))
