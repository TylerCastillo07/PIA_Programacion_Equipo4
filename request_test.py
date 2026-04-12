import requests
import json

def generar_avance_0():
    # Endpoint de la API
    url = "https://api.thecatapi.com/v1/breeds?limit=10"
    
    print("Iniciando conexión con The Cat API...")
    response = requests.get(url)
    
    # Imprimir status_code como pide la rúbrica
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        
        # Guardar respuesta cruda en archivo .json
        with open("respuesta_cruda.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print("Archivo 'respuesta.json' generado con éxito.")
    else:
        print("Error en la conexión.")  

if __name__ == "__main__":  
    generar_avance_0()
