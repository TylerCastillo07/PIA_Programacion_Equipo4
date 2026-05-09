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

El proyecto ha pasado de la simple gestión de datos a la generación de conocimiento estadístico con el **SCRIPT 2 FINAL** . El sistema no solo calcula promedios, sino que analiza la distribución completa de las variables para entender mejor el comportamiento de las razas.  Métricas Implementadas por Variable:Para las variables de Inteligencia, Energía, Adaptabilidad y Peso, el script genera:  Media (Promedio): El valor central aritmético de la muestra.  Mediana: El valor que divide los datos exactamente a la mitad, útil para detectar sesgos.  Moda: Identifica el nivel más frecuente en las razas (ej. ¿Cuál es el nivel de inteligencia más común en el mundo felino?).Rango: La dispersión total entre el valor mínimo y máximo registrado.  Tablas de Frecuencia: Un desglose detallado que cuenta cuántas razas pertenecen a cada nivel (del 1 al 5), permitiendo ver la concentración de datos en categorías específicas.

El proyecto sigue una arquitectura modular para asegurar la limpieza y mantenimiento del código:
* `main.py`: Orquestador principal del flujo.
* `src/api_client.py`: Maneja la conexión y peticiones GET a la API.
* `src/cleaner.py`: Realiza la limpieza profunda, aplanamiento y normalización.
* `src/validators.py`: Contiene los patrones de Regex para validar IDs, nombres y niveles.
* `src/utils.py`: Funciones auxiliares para la interfaz de usuario.
* `src/script1.py`: Orquestador
* `script2.py`: Orquestador del análisis estadístico y generación de gráficas, reportes Excel.
* `src/analysis.py`: Módulo que calcula media, mediana, moda, rango y tablas de frecuencia (usando Counter).
* `src/visualizations.py`: Genera las 4 gráficas requeridas (Histograma, Barras, Dispersión y Pastel)
* `src/results/`: Almacena el archivo statistics.json con los cálculos finales.
* `src/datasheet.py`: Generador del reporte en Excel con múltiples hojas (Datos, Estadísticas y Frecuencias).
* `data/raw/`: Almacena el JSON original tal cual llega de la API.
* `data/clean/`: Almacena el resultado final procesado.
* `data/figures/`: Almacena las gráficas generadas en formato PNG.

Archivod Generados:
* Reporte JSON (results/statistics.json): Resumen digital de todos los cálculos.
* Reporte Excel (results/excel/Analisis_Felino_Equipo4.xlsx): Reporte tabular profesional con múltiples hojas.
* Visualizaciones (results/plots/): Gráficas en formato PNG con títulos y leyendas claras

## Cómo ejecutar el script
Para correr este proyecto en tu computadora local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TylerCastillo07/PIA_Programacion_Equipo4.git](https://github.com/TylerCastillo07/PIA_Programacion_Equipo4.git)
2. **Instalar dependencias:**
   Este proyecto utiliza la librería `requests` para la comunicación con la API.
   ```bash
   pip install requests
   pip install requests matplotlib
   pip install pandas openpyxl
