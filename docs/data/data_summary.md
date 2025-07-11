# 📊 Reporte de Datos

Este documento presenta un análisis exploratorio limitado de los datos disponibles, correspondiente a la etapa inicial del proyecto **Diagnóstico Tributario Inteligente**. Dado que el volumen actual de datos es reducido (tres formularios tributarios en PDF), este reporte tiene carácter **estructural y demostrativo**.

---

## 📌 Resumen general de los datos

- **Cantidad de observaciones**: 3 formularios (1 IVA, 1 Renta, 1 Retefuente)
- **Cantidad de variables estructuradas extraídas**: 16 columnas (metadatos, campos tributarios, métricas de extracción)
- **Tipo de variables**:  
  - Categóricas: tipo_declaracion, fuente_pdf, metodo_extraccion  
  - Numéricas: valor_maximo, valores_encontrados, saldo_a_pagar_o_favor  
  - Temporales: fecha_procesamiento, período  
- **Valores faltantes**: No se presentan valores nulos en esta etapa, pero algunas casillas no están presentes en todos los formularios debido a su naturaleza (e.g. el campo `iva_descontable` no existe en el formulario de Renta).
- **Distribución de los tipos de declaración**:
  - IVA: 1
  - Renta: 1
  - Retefuente: 1

---

## 🧪 Resumen de calidad de los datos

- **Valores faltantes**:  
  - Variables como `retenciones_practicadas` o `iva_descontable` están ausentes en los formularios donde no aplican.
- **Valores extremos**:  
  - Se detectó un valor de `$850,000,000` en ingresos brutos (Renta), dentro de un rango razonable para personas jurídicas.
- **Errores detectados**:  
  - Ninguno estructural; sin embargo, el volumen actual no permite evaluar errores típicos.
- **Duplicados**:  
  - No se presentan formularios repetidos.
- **Acciones tomadas**:  
  - Validación manual de extracción campo a campo.
  - Conversión de valores monetarios a tipo numérico flotante.
  - Normalización de fechas y rutas de archivo.

---

## 🎯 Variable objetivo

Dado que este proyecto no tiene como objetivo principal una predicción cuantitativa, **la variable objetivo se asocia conceptualmente al campo `alertas_generadas`**, es decir, el número de inconsistencias o riesgos detectados por el sistema.

- **Distribución actual**:  
  - No se ha generado un conjunto de alertas aún, por lo que no se cuenta con valores reales.
  - En versiones futuras, esta variable puede ser binaria (riesgo/no riesgo) o continua (número de alertas).

---

## 🔍 Variables individuales

### Ejemplos:

- **`valor_maximo`**
  - Tipo: numérico continuo
  - Descripción: mayor valor monetario detectado en el texto del formulario.
  - Rango observado: $13,000,000 – $850,000,000
  - Transformaciones: escalar a miles/millones para visualización.

- **`tipo_declaracion`**
  - Tipo: categórica nominal
  - Valores: `IVA`, `RENTA`, `RETEFUENTE`
  - Frecuencia: 1 por cada tipo
  - Observación: en futuros análisis, podría usarse como variable de segmentación.

- **`calidad_extraccion`**
  - Tipo: ordinal
  - Valores esperados: `Alta`, `Media`, `Baja`
  - Distribución actual: todos los casos reportan `Alta` por haber sido seleccionados manualmente.

---

## 🧮 Ranking de variables

Dado que aún no se ha construido un modelo predictivo ni se cuenta con suficientes observaciones, no se presenta ranking de importancia. Sin embargo, variables candidatas relevantes para un modelo futuro incluyen:

- `saldo_a_pagar_o_favor`
- `iva_descontable`
- `retenciones_practicadas`
- `valor_maximo`
- `tipo_declaracion`

Cuando el sistema cuente con datos anotados y múltiples formularios por contribuyente, se podrán aplicar:
- **Correlación** con `alertas_generadas`
- **Feature importance** vía modelos de árbol
- **PCA** para reducción dimensional

---

## 🔗 Relación entre variables explicativas y variable objetivo

Por limitaciones de datos, no es posible graficar correlaciones ni ajustar modelos lineales en esta etapa. No obstante, se contempla lo siguiente para fases posteriores:

- **Matriz de correlación** entre valores monetarios y cantidad de alertas
- **Modelos de regresión o clasificación** para estimar riesgo tributario
- **Visualización** mediante gráficos de dispersión y boxplots por tipo de formulario

---

## Anotaciones

El presente reporte demuestra la estructura y potencial de análisis de los datos extraídos.  
Sin embargo, debido al **volumen extremadamente limitado** de entradas disponibles (3 documentos), **no es posible realizar un análisis exploratorio estadístico representativo ni modelado predictivo**.  
En su lugar, se recomienda generar o incorporar un conjunto de datos más amplio (real o sintético) que permita aplicar análisis y validaciones en fases posteriores del proyecto.