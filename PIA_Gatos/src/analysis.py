import statistics as stats

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
