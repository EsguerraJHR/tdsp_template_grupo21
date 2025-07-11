# 📘 Diccionario de Datos – Declaraciones Tributarias Consolidadas

**Descripción general:**  
Este dataset consolidado contiene información extraída automáticamente de formularios tributarios oficiales de la DIAN (IVA, Renta, Retefuente) en formato PDF. Los datos han sido estructurados mediante scripts de procesamiento, con el objetivo de construir un sistema de diagnóstico tributario inteligente para personas jurídicas en Colombia.

---

## 🗂️ Variables del Dataset Consolidado

| Variable                  | Descripción                                                                 | Tipo de dato | Rango / Valores posibles               | Fuente de datos                              |
|--------------------------|------------------------------------------------------------------------------|--------------|----------------------------------------|----------------------------------------------|
| `fuente_pdf`             | Nombre del archivo PDF original                                              | String       | `renta.pdf`, `iva.pdf`, `Retefuente.pdf` | Archivos PDF de declaraciones                |
| `ruta_completa`          | Ruta absoluta al archivo PDF                                                 | String       | Path completo                          | Sistema de archivos                          |
| `tamano_archivo_mb`      | Tamaño del archivo en megabytes                                              | Float        | 0.1 – 10.0                              | Metadatos del archivo                        |
| `fecha_procesamiento`    | Fecha y hora de procesamiento del archivo                                    | DateTime     | `YYYY-MM-DD HH:MM:SS`                   | Sistema de procesamiento                     |
| `nit`                    | Número de Identificación Tributaria del declarante                           | String       | 9 – 10 dígitos                          | Formulario DIAN                              |
| `razon_social`           | Razón social de la persona jurídica                                          | String       | Alfanumérico                            | Formulario DIAN                              |
| `tipo_declaracion`       | Tipo de declaración tributaria                                               | String       | `IVA`, `RETEFUENTE`, `RENTA`           | Análisis del formulario                      |
| `año`                    | Año gravable de la declaración                                               | Integer      | 2019 – 2025                             | Formulario DIAN                              |
| `periodo`                | Período fiscal de la declaración                                             | String       | `MM-YYYY` o `YYYY-MM`                   | Formulario DIAN                              |
| `casilla_X` (varias)     | Campos monetarios clave (varían según formulario)                            | Float        | ≥ 0                                     | Casillas específicas de cada formulario      |
| `valores_encontrados`    | Cantidad de valores monetarios detectados en el texto extraído               | Integer      | 0 – 200                                 | Extracción de texto                          |
| `valor_maximo`           | Valor monetario máximo detectado en el documento                             | Float        | ≥ 0                                     | Análisis de texto                            |
| `casillas_identificadas` | Número de casillas relevantes detectadas en el formulario                    | Integer      | 0 – 50                                  | Análisis de formulario                       |
| `longitud_texto`         | Longitud del texto extraído (en caracteres)                                  | Integer      | 0 – 50,000                              | Extracción de PDF                            |
| `metodo_extraccion`      | Método utilizado para la extracción                                           | String       | `PyPDF2`, `pdfplumber`, `SmolDocling`   | Sistema de procesamiento                     |
| `calidad_extraccion`     | Nivel de calidad de la extracción estimado automáticamente                   | String       | `Alta`, `Media`, `Baja`                 | Evaluación automática basada en métricas     |
| `alertas_generadas`      | Número de alertas emitidas por el motor de validación                        | Integer      | ≥ 0                                     | Motor de reglas                              |
| `saldo_a_pagar_o_favor`  | Resultado final: valor a pagar (positivo) o a favor (negativo)               | Float        | Positivo / Negativo / Cero              | Casillas de cálculo o campo específico       |
| `retenciones_practicadas`| Total de retenciones en formulario 350                                       | Float        | ≥ 0                                     | Casilla correspondiente                      |
| `iva_descontable`        | Valor de IVA descontable en formulario 300                                   | Float        | ≥ 0                                     | Casilla correspondiente                      |

---

## 📝 Notas técnicas

- **Casillas por tipo de formulario**:
  - **Formulario 110 – Renta**: ingresos brutos, costos, gastos, renta líquida, impuesto causado, anticipos, saldo.
  - **Formulario 300 – IVA**: total ingresos, IVA generado, IVA descontable, saldo a pagar.
  - **Formulario 350 – Retefuente**: base sujeta, retenciones practicadas, retenciones consignadas, diferencia.

- **Extracción**: se utiliza `pdfplumber` y `regex` para convertir los formularios en texto estructurado.

- **Calidad de extracción**: se estima en función de la longitud del texto, la cantidad de valores detectados y la coherencia con plantillas esperadas.

- **Limitaciones conocidas**:
  - Algunas casillas pueden no detectarse por mala estructuración del PDF.
  - En formularios escaneados o no seleccionables, los datos pueden perderse o unirse.
  - El dataset incluye solo **tres documentos**, lo cual limita el valor estadístico pero permite validar estructura y flujo técnico.

---

## ✅ Uso recomendado

- Validación estructural de formularios PDF.
- Pruebas unitarias del pipeline de extracción y consolidación.
- Ejecución de pruebas del motor de reglas sobre declaraciones simuladas.
- Desarrollo incremental de un sistema de diagnóstico tributario inteligente basado en arquitectura modular.