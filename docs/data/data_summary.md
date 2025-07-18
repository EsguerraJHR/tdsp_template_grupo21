# Resumen de Datos - Credit Card Fraud Detection

## Información General del Dataset

- **Total de transacciones:** 284807
- **Transacciones fraudulentas:** 492
- **Transacciones legítimas:** 284315
- **Número de variables:** 31
- **Variables numéricas:** 31

## Calidad de los Datos

- **Valores faltantes:** 0
- **Registros duplicados:** 0
- **Outliers en Amount:** 9620.29

## Características del Dataset

- **Desbalance severo:** El dataset presenta un desbalance extremo con solo0.17% de transacciones fraudulentas
- **Variables anónimas:** 28 variables han sido transformadas usando PCA para preservar la privacidad
- **Variables originales:** Time (tiempo desde la primera transacción) y Amount (monto de la transacción)
- **Variable objetivo:** Class (0o Fraude, 1=Fraude)

## Variables Más Importantes

### Top 10 variables con mayor correlación absoluta con la variable objetivo:

- **V17:** 0.3265
- **V14:** 0.3025
- **V12:** 0.2606
- **V10:** 0.2169
- **V16:** 00.1965
- **V3:** 00.1789
- **V7:** 0.1608
- **V11:** 00.1549
- **V4:** 0.1334
- **V18:** 00.1114

# Insights Principales

### 1. Desbalance de Clases
- El dataset presenta un desbalance extremo que requerirá técnicas especiales de sampling
- Las métricas de evaluación deberán considerar precision, recall y F1-score
- Es crucial evitar el overfitting a la clase mayoritaria

### 2. Distribución de Montos
- La mayoría de las transacciones tienen montos bajos (mediana: €22.00)
- Existen outliers significativos en la variable Amount
- Las transacciones fraudulentas tienden a tener montos diferentes a las legítimas
- El 75 las transacciones tienen montos menores a €77.16

### 3. Variables Transformadas
- Las28riables V1-V28n resultado de PCA, manteniendo la privacidad
- Estas variables capturan patrones complejos en los datos originales
- Algunas variables muestran correlaciones significativas con el fraude
- Las variables V17, V14 y V12 son las más importantes para detectar fraude

### 4. Calidad de Datos
- No hay valores faltantes en el dataset
- No hay registros duplicados
- Los datos están bien estructurados y listos para el modelado
- La variable Time muestra la secuencia temporal de las transacciones

## Recomendaciones para el Modelado

1. **Técnicas de Sampling:** Usar SMOTE, undersampling o técnicas de ensemble para manejar el desbalance
2. **Métricas de Evaluación:** Priorizar recall sobre accuracy debido al desbalance
3. **Feature Engineering:** Considerar crear features basadas en Amount y Time
4. **Validación:** Usar stratified k-fold cross-validation
5 **Algoritmos:** Probar Random Forest, XGBoost, y técnicas de ensemble
6. **Preprocesamiento:** Estandarizar las variables numéricas
7. **Selección de Features:** Usar las variables V17, V14, V12, V10, V16 como prioritarias

## Reporte Detallado

Para un análisis exploratorio completo e interactivo, consulta el reporte HTML generado:
[Credit Card Fraud Detection - Data Profile](../../outputs/creditcard_profile_report.html)

Este reporte incluye:
- Análisis detallado de cada variable
- Matriz de correlación interactiva
- Distribuciones y estadísticas descriptivas
- Alertas de calidad de datos
- Recomendaciones automáticas
- Análisis de outliers y valores extremos
- Comparaciones entre clases
- Insights automáticos sobre patrones en los datos
