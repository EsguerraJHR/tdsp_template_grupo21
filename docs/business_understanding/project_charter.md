# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Diagnóstico tributario inteligente

## Objetivo del Proyecto

Construir un diagnóstico de cumplimiento y riesgo que analiza las declaraciones tributarias (Renta, IVA, Retención) de un cliente, contrasta las alertas generadas con jurisprudencia y pronunciamientos oficiales, y responde a preguntas clave sobre plazos, consistencia de valores, saldos a favor y riesgos de fiscalización

## Alcance del Proyecto

### Incluye:

#### Descripción de los datos disponibles:

El proyecto cuenta con tres fuentes de datos principales:

1. Datos Transaccionales: Se dispone de un conjunto de declaraciones tributarias reales en formato PDF, incluyendo el Formulario 300 (IVA), el Formulario 350 (Retención en la Fuente) y el Formulario 110 (Renta). Estos son los insumos primarios para el diagnóstico.
2. Base de Conocimiento Jurídico: Se cuenta con una base de conocimiento jurídico-tributaria ya procesada y disponible en formato Markdown. Esta base de datos curada incluye jurisprudencia relevante, conceptos y pronunciamientos oficiales de la DIAN, y extractos de la normativa tributaria. Servirá como la fuente de verdad para el agente de IA en la fase de investigación.
3. Lógica de Negocio: Se tienen las plantillas maestras de validación en formato Excel, las cuales contienen las reglas de negocio, cruces de información y checklists que se deben replicar en el motor de diagnóstico del sistema.
  
# Descripción de los resultados esperados:

Un Sistema de Diagnóstico Inteligente implementado en Python, compuesto por tres módulos principales:

1. Un módulo de extracción de datos que utiliza el modelo de lenguaje de visión SmolDocling para convertir los formularios tributarios en PDF (110, 300, 350) a un formato de datos estructurado.

2. Un motor de reglas de validación que procesa los datos extraídos para identificar y generar una lista de alertas sobre riesgos, inconsistencias y oportunidades.

3. Un agente de razonamiento (LLM) que analiza las alertas generadas, las prioriza según su criticidad y genera explicaciones fundamentadas para los hallazgos más importantes.

4. Un API de diagnóstico funcional y desplegada utilizando FastAPI. Este API recibirá los datos de una declaración y devolverá un informe completo del análisis en formato JSON.

- [Criterios de éxito del proyecto]

### Excluye:

- [Descripción de lo que no está incluido en el proyecto]

## Metodología

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas | del 1 de mayo al 15 de mayo |
| Preprocesamiento, análisis exploratorio | 4 semanas | del 16 de mayo al 15 de junio |
| Modelamiento y extracción de características | 4 semanas | del 16 de junio al 15 de julio |
| Despliegue | 2 semanas | del 16 de julio al 31 de julio |
| Evaluación y entrega final | 3 semanas | del 1 de agosto al 21 de agosto |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- [Nombre y cargo del líder del proyecto]
- [Nombre y cargo de los miembros del equipo]

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
