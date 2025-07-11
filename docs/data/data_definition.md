# 📄 Definición de los Datos

## 🧭 Origen de los Datos

### Fuentes de datos principales

El proyecto **Diagnóstico Tributario Inteligente** se apoya en tres fuentes principales:

---

### 1. Datos Transaccionales

Conjunto de declaraciones tributarias reales en formato PDF, correspondientes a personas jurídicas. Incluye:

- **Formulario 300** (Impuesto sobre las Ventas – IVA)
- **Formulario 350** (Retención en la Fuente)
- **Formulario 110** (Impuesto sobre la Renta)

Estos formularios constituyen los insumos primarios para la detección de alertas tributarias, identificación de inconsistencias y evaluación de cumplimiento.

---

### 2. Base de Conocimiento Jurídico

Repositorio de conocimiento jurídico-tributario estructurado en archivos Markdown, que incluye:

- Jurisprudencia relevante
- Conceptos y pronunciamientos oficiales de la DIAN
- Extractos seleccionados de normativa tributaria

Esta base curada actúa como **fuente de verdad** para el agente de razonamiento, permitiendo explicar alertas y respaldarlas con normatividad vigente.

---

### 3. Lógica de Negocio

Plantillas de validación en formato Excel que contienen:

- Reglas de negocio codificadas (e.g. plazos, cruces, saldos)
- Checklists tributarios
- Casos de referencia

Estas plantillas definen las validaciones clave que el motor del sistema debe replicar para emitir alertas y priorizar hallazgos.

---

## ⚙️ Método de Obtención

Los datos se extraen a través de un pipeline propio de procesamiento de PDFs implementado en Python. Actualmente se utilizan las librerías:

- `pdfplumber`
- `PyMuPDF`
- `re` (expresiones regulares)

El extractor transforma los formularios en texto estructurado y lo convierte en registros tabulares.  
Aunque en etapas futuras se contempla el uso de modelos como **SmolDocling** para formularios más complejos, esta integración aún no ha sido implementada.

---

## 📜 Especificación de Scripts para la Carga de Datos

### Script principal de adquisición

- **Archivo**: `scripts/data_acquisition/main.py`  
- **Función**: Procesa automáticamente todos los archivos PDF de declaraciones tributarias

### Módulo de procesamiento

- **Ubicación**: `src/diagnostico_tributario/procesador.py`  
- **Función clave**: `procesar_un_pdf()` – Extrae texto y datos estructurados de cada formulario.

---

## 🔄 Pipeline de Procesamiento

El flujo implementado consta de las siguientes etapas:

1. **Extracción de texto**: Conversión del PDF a texto plano estructurado
2. **Análisis tributario**: Identificación de tipo de formulario, NIT, período, y valores monetarios clave
3. **Consolidación**: Generación de un único dataset estructurado en formato CSV
4. **Validación**: Revisión de la calidad de extracción y presencia de campos clave

---

## 📁 Rutas y Archivos

### Ubicación de los archivos de origen
   data/raw/declaraciones_pdf/
   ├── iva.pdf          # Formulario 300 - IVA
   ├── renta.pdf        # Formulario 110 - Renta
   └── Retefuente.pdf   # Formulario 350 - Retefuente

- **Formato**: PDF con texto seleccionable
- **Contenido**: Formularios oficiales de la DIAN diligenciados
- **Tamaño promedio**: 3.000–5.000 caracteres por archivo

---

## 🔧 Transformación y Limpieza

- **Extracción de texto**: Uso de múltiples librerías para mayor compatibilidad
- **Análisis estructural**: Identificación automática de patrones tributarios (e.g. ingresos, retenciones)
- **Validación de calidad**: Comprobación de completitud y coherencia de datos
- **Estandarización**: Conversión a formatos uniformes para fechas, montos y códigos
- **Consolidación**: Unión de todos los formularios en un único archivo CSV
- **Enriquecimiento**: Cálculo de métricas como número de valores detectados, longitud de texto y calidad de extracción

---

## 📦 Base de Datos de Destino

- **Ruta de salida**: `data/processed/declaraciones_consolidadas.csv`
- **Formato**: CSV con ~16 columnas estructuradas

### Principales campos:

- Metadatos del archivo: nombre, ruta, tamaño, fecha
- Datos clave: NIT, tipo de declaración, año, período
- Valores monetarios extraídos
- Métricas de extracción: longitud del texto, valores identificados, calidad

---

## 🎯 Criterios de Calidad Esperados

Dado el carácter prototípico del sistema y la disponibilidad actual de datos reales (solo tres formularios), el objetivo principal es **validar la estructura, consistencia y funcionamiento del flujo de extracción**.

Los criterios definidos para futuras fases incluyen:

- **Precisión esperada de extracción**: ≥ 95% en campos numéricos clave
- **Cobertura mínima de reglas de validación**: 15 reglas, una vez el sistema se escale a datos reales o sintéticos
- **Tiempo de procesamiento por archivo**: Menor a 3 minutos

---

## ⚠️ Nota Importante

Actualmente, el dataset incluye **únicamente tres archivos reales** (uno por tipo de declaración). Por tanto, **no es posible realizar análisis exploratorio ni validar métricas de desempeño generalizables**.  
Esta fase se enfoca en demostrar la viabilidad técnica, la modularidad del sistema y la preparación para escalar en futuras etapas con más datos.
