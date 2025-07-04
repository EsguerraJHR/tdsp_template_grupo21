# Diccionario de datos

## Base de datos 1

**Agregar una descripción de la tabla o fuente de datos.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| variable_1 | Descripción de la variable 1 | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| variable_2 | Descripción de la variable 2 | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| variable_3 | Descripción de la variable 3 | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| variable_4 | Descripción de la variable 4 | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| variable_5 | Descripción de la variable 5 | Tipo de dato | Rango/Valores posibles | Fuente de datos |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

## Base de datos 2

**Agregar una descripción de la tabla o fuente de datos.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| variable_1 | Descripción de la variable 1 | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| variable_2 | Descripción de la variable 2 | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| variable_3 | Descripción de la variable 3 | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| variable_4 | Descripción de la variable 4 | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| variable_5 | Descripción de la variable 5 | Tipo de dato | Rango/Valores posibles | Fuente de datos |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

## Declaraciones Tributarias Consolidadas

**Dataset consolidado de declaraciones tributarias procesadas mediante extracción directa de PDF. Contiene información extraída de formularios DIAN (IVA, Renta, Retención en la Fuente) para análisis de diagnóstico tributario.**

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| fuente_pdf | Nombre del archivo PDF original | String | Nombre de archivo .pdf | Archivos PDF declaraciones |
| ruta_completa | Ruta completa al archivo PDF | String | Path absoluto | Sistema de archivos |
| tamano_archivo_mb | Tamaño del archivo en megabytes | Float | 0.1 - 10.0 MB | Metadatos del archivo |
| fecha_procesamiento | Fecha y hora de procesamiento | DateTime | YYYY-MM-DD HH:MM:SS | Sistema de procesamiento |
| nit | Número de Identificación Tributaria | String | 9-10 dígitos | Formulario DIAN |
| tipo_declaracion | Tipo de declaración tributaria | String | IVA, RENTA, RETEFUENTE, GENERAL | Análisis de contenido |
| año | Año gravable de la declaración | String | 2020-2024 | Formulario DIAN |
| periodo | Período de la declaración | String | YYYY-MM | Formulario DIAN |
| casilla_24_ingresos_5pct | Ingresos gravados tarifa 5% | Integer | 0 - 999,999,999,999 | Casilla 24 formulario |
| casilla_57_iva_descontable | IVA descontable | Integer | 0 - 999,999,999,999 | Casilla 57 formulario |
| valores_encontrados | Cantidad de valores monetarios extraídos | Integer | 0 - 100 | Análisis de texto |
| valor_maximo | Valor monetario máximo encontrado | Integer | 0 - 999,999,999,999 | Análisis de texto |
| casillas_identificadas | Número de casillas identificadas | Integer | 0 - 50 | Análisis de formulario |
| longitud_texto | Longitud del texto extraído | Integer | 0 - 50,000 caracteres | Extracción de PDF |
| metodo_extraccion | Método usado para extracción | String | Extracción_Directa_PDF | Sistema de procesamiento |
| calidad_extraccion | Calidad de la extracción | String | Alta, Media, Baja | Evaluación automática |

### Notas Técnicas:

- **Fuente de datos**: Formularios oficiales DIAN en formato PDF
- **Método de extracción**: PyPDF2/pdfplumber para extracción directa de texto
- **Procesamiento**: Análisis automático con regex y NLP básico
- **Calidad**: Determinada por longitud de texto extraído y cantidad de elementos identificados
- **Limitaciones**: Algunos valores monetarios pueden estar concatenados debido a la estructura del PDF

### Casos Especiales:

- **NITs vacíos**: Cuando no se puede extraer el NIT del formulario
- **Valores concatenados**: Números largos que representan múltiples valores unidos
- **Tipo IVA por defecto**: Algunos formularios de renta se clasifican como IVA debido a palabras clave

### Uso Recomendado:

Este dataset es ideal para:
- Análisis exploratorio de declaraciones tributarias
- Identificación de patrones en montos declarados
- Validación de consistencia en formularios
- Desarrollo de modelos de diagnóstico tributario

