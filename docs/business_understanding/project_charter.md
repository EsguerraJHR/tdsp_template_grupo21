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
  
#### Descripción de los resultados esperados:

Un Sistema de Diagnóstico Inteligente implementado en Python, compuesto por tres módulos principales:

1. Un módulo de extracción de datos que utiliza el modelo de lenguaje de visión SmolDocling para convertir los formularios tributarios en PDF (110, 300, 350) a un formato de datos estructurado.

2. Un motor de reglas de validación que procesa los datos extraídos para identificar y generar una lista de alertas sobre riesgos, inconsistencias y oportunidades.

3. Un agente de razonamiento (LLM) que analiza las alertas generadas, las prioriza según su criticidad y genera explicaciones fundamentadas para los hallazgos más importantes.

4. Un API de diagnóstico funcional y desplegada utilizando FastAPI. Este API recibirá los datos de una declaración y devolverá un informe completo del análisis en formato JSON.

#### Criterios de éxito del proyecto:

1. Precisión de Extracción: El módulo de extracción de datos debe alcanzar una precisión igual o superior a 95% en la identificación y transcripción de los campos numéricos clave de los formularios.

2. Cobertura del Motor de Reglas: El motor de reglas debe implementar y validar correctamente un mínimo de 15 reglas de negocio distintas, cubriendo plazos, consistencia entre los tres formularios y detección de saldos a favor.

3. Calidad del Razonamiento: El agente de razonamiento (LLM) debe priorizar correctamente el 90% de las alertas en los casos de prueba y generar explicaciones coherentes y fundamentadas para los riesgos de mayor impacto.
   
5. Rendimiento del API: El API de diagnóstico desplegada debe mantener un tiempo de respuesta promedio inferior a 3 minutos por solicitud.

### Excluye:

El desarrollo de una interfaz gráfica de usuario para la carga de archivos o la visualización de resultados. La interacción con el sistema será exclusivamente a través del API.

La emisión de conceptos, opiniones o asesorías que sean legalmente vinculantes. La herramienta es un sistema de apoyo para expertos.

El agente de investigación jurídica no realizará búsquedas en tiempo real sobre toda la base de datos de jurisprudencia; operará sobre una base de conocimiento curada y específica para las reglas implementadas.

## Metodología

El proyecto se ejecutará bajo el marco de la metodología Team Data Science Process (TDSP). El desarrollo se gestionará en un repositorio de GitHub utilizando la plantilla proporcionada. Las herramientas tecnológicas principales serán Python junto con sus librerías (Pandas, Scikit-learn) para el análisis y modelado y FastAPI para el despliegue del servicio de diagnóstico.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas | del 19 de junio al 3 de julio |
| Preprocesamiento, análisis exploratorio | 1 semana  | del 4 al 10 de julio |
| Modelamiento y extracción de características | 1 semana | del 11 al 17 de julio |
| Despliegue | 1 semana | del 18 al 24 de julio |
| Evaluación y entrega final | 1 semana | del 25 al 31 de julio |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- Hernando Castro Arana
- Nicolas Amado Aristizabal
- Diego Alejandro Feliciano Ramos

## Presupuesto

El presupuesto asignado para la ejecución de este proyecto es de 25$ USD. 

## Stakeholders

##### Nombre y cargo de los stakeholders:

Abogados tributaristas

Contadores y revisores fiscales

Gerentes financieros y de impuestos

##### Descripción de la relación con los stakeholders:

Son los beneficiarios y usuarios finales de la herramienta. El sistema está diseñado para integrarse en su flujo de trabajo, potenciar su capacidad de análisis y optimizar sus procesos de cumplimiento tributario o diagnósticos de riesgo y cumplimiento tributario.

#### Expectativas de los stakeholders:

Esperan una herramienta que automatice la extracción de datos de los PDF, reduzca significativamente el tiempo de análisis manual, minimice el riesgo de error humano, y proporcione diagnósticos precisos y rápidos que les permitan tomar decisiones informadas, anticipar riesgos y defender los intereses de sus clientes o empresas.

## Aprobaciones

Hernan do Castro Arana
