# Registro de Errores y Manejo de Excepciones - Equipo 4

Este documento detalla los errores potenciales identificados durante el desarrollo del Script 1 y cómo se implementó su solución para hacer el sistema robusto.

## 1. Errores de Conexión (API)
- **Error identificado:** `requests.exceptions.ConnectionError`
- **Causa:** El usuario no tiene internet o el servidor de TheCatAPI está caído.
- **Manejo:** Se implementó un bloque `try-except` en `api_client.py` que captura el error y evita que el programa se detenga, mostrando un mensaje amigable al usuario.

## 2. Errores de Conversión de Tipos
- **Error identificado:** `ValueError` e `IndexError`
- **Causa:** Al intentar extraer el peso de la cadena "3 - 5 kg", la lista de números podría estar vacía o el formato ser inválido.
- **Manejo:** En `cleaner.py`, se rodeó la conversión de `int()` con un `try-except`. Si el dato es inválido, se asigna un valor por defecto de `0`.

## 3. Errores de Archivos (I/O)
- **Error identificado:** `FileNotFoundError` o `PermissionError`
- **Causa:** Intentar guardar el JSON en una carpeta que no existe o sin permisos de escritura.
- **Manejo:** Se utilizó `os.makedirs(exist_ok=True)` y un bloque `try-except IOError` en el `main.py` para asegurar que el guardado sea seguro.

## 4. Datos Faltantes (Nulos)
- **Error identificado:** `KeyError`
- **Causa:** La API a veces no envía todos los campos (ej. un gato sin campo 'origin').
- **Manejo:** Se sustituyó el acceso directo por el método `.get("campo", "valor_por_defecto")`.
