# Definición de los datos

## Origen de los datos

### Fuentes de datos principales

El proyecto **Diagnóstico tributario inteligente** cuenta con tres fuentes de datos principales:

1. **Datos Transaccionales**: Conjunto de declaraciones tributarias reales en formato PDF, incluyendo:
   - Formulario 300 (IVA)
   - Formulario 350 (Retención en la Fuente) 
   - Formulario 110 (Renta)
   
   Estos constituyen los insumos primarios para el diagnóstico tributario.

2. **Base de Conocimiento Jurídico**: Base de conocimiento jurídico-tributaria procesada y disponible en formato Markdown, que incluye:
   - Jurisprudencia relevante
   - Conceptos y pronunciamientos oficiales de la DIAN
   - Extractos de la normativa tributaria
   
   Sirve como fuente de verdad para el agente de IA en la fase de investigación.

3. **Lógica de Negocio**: Plantillas maestras de validación en formato Excel que contienen:
   - Reglas de negocio
   - Cruces de información
   - Checklists para replicar en el motor de diagnóstico

### Método de obtención

Los datos se obtienen mediante el módulo de extracción que utiliza el modelo de lenguaje de visión **SmolDocling** para convertir los formularios tributarios en PDF a formato de datos estructurado.

## Especificación de los scripts para la carga de datos

### Script principal de adquisición

- **Archivo**: `scripts/data_acquisition/main.py`
- **Función**: Procesamiento automatizado de los PDFs tributarios
- **Módulo de procesamiento**: `src/diagnostico_tributario/procesador.py`
- **Función clave**: `procesar_un_pdf()` - Extrae texto y datos estructurados de cada formulario

### Pipeline de procesamiento

El pipeline implementa las siguientes etapas:
1. **Extracción de texto**: Conversión de PDF a texto estructurado
2. **Análisis tributario**: Identificación de tipos de declaración, NITs, valores monetarios
3. **Consolidación**: Generación de dataset unificado en formato CSV
4. **Validación**: Verificación de calidad de extracción

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

**Ubicación de archivos de origen:**
- `data/raw/declaraciones_pdf/`
  - `iva.pdf` - Formulario 300 (IVA)
  - `renta.pdf` - Formulario 110 (Renta)
  - `Retefuente.pdf` - Formulario 350 (Retención en la Fuente)

**Estructura de archivos de origen:**
- **Formato**: PDF con texto seleccionable
- **Contenido**: Formularios tributarios oficiales de la DIAN
- **Tamaño promedio**: 3,000-5,000 caracteres por archivo

**Procedimientos de transformación y limpieza:**
1. **Extracción de texto**: Utilización de múltiples librerías (PyPDF2, pdfplumber, pymupdf)
2. **Análisis inteligente**: Identificación automática de patrones tributarios
3. **Validación de calidad**: Verificación de completitud y coherencia de datos extraídos
4. **Estructuración**: Conversión a formato tabular con campos estandarizados

### Base de datos de destino

**Ubicación de datos procesados:**
- `data/processed/declaraciones_consolidadas.csv`

**Estructura de la base de datos de destino:**
- **Formato**: CSV con 16 columnas estructuradas
- **Campos principales**:
  - Metadatos del archivo (nombre, ruta, tamaño, fecha)
  - Datos extraídos (NITs, tipo de declaración, año, período)
  - Valores monetarios identificados
  - Métricas de calidad (longitud de texto, valores encontrados, calidad de extracción)

**Procedimientos de carga y transformación:**
1. **Consolidación**: Unión de datos de los tres formularios en un dataset único
2. **Estandarización**: Aplicación de formatos consistentes para fechas, valores monetarios y códigos
3. **Enriquecimiento**: Adición de métricas de calidad y metadatos de procesamiento
4. **Validación final**: Verificación de integridad y completitud del dataset consolidado

### Criterios de calidad esperados

El módulo de extracción debe alcanzar:
- **Precisión de extracción**: ≥95% en identificación y transcripción de campos numéricos clave
- **Cobertura de validación**: Mínimo 15 reglas de negocio implementadas
- **Tiempo de procesamiento**: <3 minutos por solicitud de diagnóstico
