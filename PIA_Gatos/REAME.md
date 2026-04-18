# PIA - Análisis Estadístico de Razas Felinas
**Equipo 4 - Integrantes:**
* Tyler Gabriel Castillo Lozano - 2163447 - **Programador**
* Monserrat Cárdenas Rodiz - 2206788 - **Analista de Datos** 
* América Michelle Vázquez Tamayo - 2191273 - **Capturista de Datos** 

**API Elegida:** [The Cat API](https://developers.thecatapi.com/)

Elegimos esta API porque ofrece datos anidados detallados sobre más de 60 razas de gatos, incluyendo métricas numéricas (del 1 al 5) sobre inteligencia, energía y salud. Esto nos permite realizar los cálculos de media, mediana y moda, así como las 4 gráficas requeridas.

*Pregunta de investigación:*
¿Existe una correlación estadística significativa entre el nivel de inteligencia de una raza de gato y su nivel de necesidades sociales o adaptabilidad?

Este proyecto es el **Script 1 FINAL** de nuestro PIA. Se conecta a una API externa de gatos, extrae la información de las razas, realiza una validación exhaustiva mediante expresiones regulares (Regex) y limpia los datos para generar un archivo JSON estructurado y listo para su análisis.

El proyecto sigue una arquitectura modular para asegurar la limpieza y mantenimiento del código:
* `main.py`: Orquestador principal del flujo.
* `src/api_client.py`: Maneja la conexión y peticiones GET a la API.
* `src/cleaner.py`: Realiza la limpieza profunda, aplanamiento y normalización.
* `src/validators.py`: Contiene los patrones de Regex para validar IDs, nombres y niveles.
* `src/utils.py`: Funciones auxiliares para la interfaz de usuario.
* `data/raw/`: Almacena el JSON original tal cual llega de la API.
* `data/clean/`: Almacena el resultado final procesado.

## Cómo ejecutar el script
Para correr este proyecto en tu computadora local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TylerCastillo07/PIA_Programacion_Equipo4.git](https://github.com/TylerCastillo07/PIA_Programacion_Equipo4.git)
