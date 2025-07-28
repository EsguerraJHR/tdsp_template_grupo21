# Despliegue de modelos
## Infraestructura

### Nombre del modelo
fraud-detection-model

### Plataforma de despliegue
Hugging Face Spaces

### Requisitos técnicos:
* Lenguaje: Python 3.11 (desarrollo), Python 3.9 (despliegue en Hugging Face)
* Bibliotecas:
    * fastapi
    * uvicorn
	* scikit-learn
	* joblib
	* imbalanced-learn (SMOTE)
	* pandas
	* gdown (para descarga de datasets)
* Hardware:
    * Requisitos mínimos del runtime de Hugging Face (CPU)

### Requisitos de seguridad:
* El entorno de Hugging Face Spaces se ejecuta de forma aislada (sandboxed)
* No se implementó autenticación o cifrado ya que la API es de uso libre para pruebas
* Para producción se recomienda agregar:
    * Autenticación con tokens o OAuth2
    * Cifrado de datos sensibles (TLS, HTTPS)

### Diagrama de arquitectura:

Mermaid: 
```mermaid
graph TD
  User[Usuario] -->|Solicita predicción| API[FastAPI en Docker]
  API -->|Usa modelo y scaler| Modelo[Modelo .joblib + scaler.pkl]
  Modelo -->|Devuelve resultado| API
  API -->|Devuelve JSON| User
  ```

### Código de despliegue

Archivo principal: app.py

Rutas de acceso a los archivos:
* app.py → contiene la definición de la API con FastAPI
* model.joblib → modelo entrenado y serializado
* scaler.pkl → objeto StandardScaler para normalizar los datos
* requirements.txt → dependencias del proyecto
* Dockerfile → define el contenedor de despliegue

### Variables de entorno:
Actualmente no se utilizan variables de entorno explícitas. Para producción se recomienda:
* MODEL_PATH=model.joblib
* SCALER_PATH=scaler.pkl
* PORT=7860

### Documentación del despliegue

Instrucciones de instalación:
* Subir los archivos del folder scripts/deployment al Space de Hugging Face
* Asegurarse de que exista el archivo Dockerfile en la raíz (con ese nombre exactamente)
* Verificar que el archivo principal se llame app.py y contenga app = FastAPI()
* Hugging Face construirá automáticamente el contenedor al detectar el Dockerfile

### Instrucciones de configuración:
* No se requiere configuración adicional
* Para customizar el puerto o nombre del archivo principal, modificar el CMD en el Dockerfile

### Instrucciones de uso:
* Acceder a la API en: https://mlds6-ftp-fraud-api.hf.space
* Usar /predict enviando un JSON con la siguiente estructura:

{
  "features": [valor1, valor2, ..., valorN]
}

Un ejemplo de petición sería el siguiente 
```
curl -X POST https://mlds6-ftp-fraud-api.hf.space/predict \
  -H "Content-Type: application/json" \
  -d '{
    "features": [472, -3.0435406239976, -3.15730712090228, 1.08846277997285, 2.2886436183814, 1.35980512966107, -1.06482252298131, 0.325574266158614, -0.0677936531906277, -0.270952836226548, -0.838586564582682, -0.414575448285725, -0.503140859566824, 0.676501544635863, -1.69202893305906, 2.00063483909015, 0.666779695901966, 0.599717413841732, 1.72532100745514, 0.283344830149495, 2.10233879259444, 0.661695924845707, 0.435477208966341, 1.37596574254306, -0.293803152734021, 0.279798031841214, -0.145361714815161, -0.252773122530705, 0.0357642251788156, 529]
  }'
```

Y su respuesta puede ser bien 0 o 1, cómo en el siguiente fragmento de respuesta:
```
{"prediction":0}
```
Donde 0 es transacción legítima y 1 es transacción fraudulenta.

* Ver la documentación interactiva en [/docs](https://mlds6-ftp-fraud-api.hf.space/docs)

### Costos de infraestructura

La ejecución del modelo se realiza en la infraestructura gratuita de Hugging Face Spaces, utilizando hardware compartido (CPU). Este entorno es ideal para aplicaciones ligeras como esta API de detección de fraude, ya que no requiere procesamiento intensivo. Hugging Face permite escalar fácilmente a opciones de pago en caso de necesitar GPU u otros recursos adicionales.
En la siguiente imagen se detallan los costos asociados al uso del hardware según el plan seleccionado:

<image src=./costohardware.png></image>

### Costos de almacenamiento y persistencia

El modelo (model.joblib) y el objeto de escalado (scaler.pkl) se almacenan directamente en el repositorio del Space. Hugging Face proporciona almacenamiento gratuito con un límite de hasta 5 GB por espacio, lo cual resulta más que suficiente para este proyecto.
No se requiere una base de datos ni almacenamiento externo, ya que todo el procesamiento es in-memory.
En esta imagen se describen los costos relacionados con el almacenamiento y la persistencia en Hugging Face:

<image src=./costopersistencia.png></image>

### Instrucciones de mantenimiento:
* Para actualizar el modelo: subir una nueva versión de model.joblib y reiniciar el Space
* Para agregar validación o autenticación: editar app.py y rehacer el build
* Para mantenimiento general: usar el panel de administración de Hugging Face Spaces (reinicio, logs, etc.)