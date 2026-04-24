import requests

def get_data(url):
    try:
        response = requests.get(url, timeout=10)
        # Lanza una excepción si el status code no es 200 (éxito)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar al servidor. Revisa tu internet.")
    except requests.exceptions.HTTPError as e:
        print(f"Error en la API (HTTP): {e}")
    except requests.exceptions.Timeout:
        print("Error: La solicitud tardó demasiado tiempo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al conectar: {e}")
    else:
        # Solo se ejecuta si el bloque try fue exitoso
        return response.json()
    return None
