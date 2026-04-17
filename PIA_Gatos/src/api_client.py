import requests

def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error en API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None
