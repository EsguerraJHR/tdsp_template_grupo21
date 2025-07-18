# Reporte del Modelo Baseline - Detección de Fraude de Tarjetas de Crédito

## Descripción del Modelo

El modelo baseline para la detección de fraude de tarjetas de crédito se estableció utilizando **Logistic Regression** como punto de referencia inicial. Este modelo lineal proporciona una línea base sólida para comparar el rendimiento de modelos más complejos.

### Características del Modelo Baseline
- **Algoritmo**: Regresión Logística
- **Configuración**: max_iter=300, random_state=42
- **Dataset**: 10% muestreado (5,696 transacciones)
- **Balanceo**: SMOTE aplicado al conjunto de entrenamiento

## Variables de Entrada

### Características Utilizadas
1. **V1-V28**: Variables anonimizadas (componentes principales)
2. **Amount**: Monto de la transacción
3. **Time**: Tiempo desde la primera transacción

### Preprocesamiento
- **Escalado**: StandardScaler aplicado a todas las variables numéricas
- **Balanceo**: SMOTE para equilibrar las clases en entrenamiento
- **División**: 80% entrenamiento, 20% test con estratificación

## Variable Objetivo

- **Nombre**: `Class`
- **Valores**: 
  - 0: Transacción legítima
  - 1: Transacción fraudulenta
- **Distribución**: Altamente desbalanceada (99.9% legítimas, 0.1% fraudulentas)

## Evaluación del Modelo

### Métricas de Evaluación

Se utilizaron las siguientes métricas para evaluar el rendimiento:

1. **Accuracy**: Precisión general del modelo
2. **Precision**: Proporción de predicciones positivas correctas
3. **Recall**: Proporción de casos positivos reales identificados
4. **F1-Score**: Media armónica de precisión y recall
5. **AUC-ROC**: Área bajo la curva ROC
6. **Validación Cruzada**: StratifiedKFold con 3 folds

### Resultados de Evaluación

| Métrica | Valor Test | CV Mean | CV Std |
|---------|------------|---------|--------|
| **Accuracy** | 0.9719 | - | - |
| **Precision** | 0.0303 | - | - |
| **Recall** | 1.0000 | - | - |
| **F1-Score** | 0.0588 | 0.9524 | 0.0005 |
| **AUC** | 0.9997 | 0.9921 | 0.0003 |

### Análisis de Clases

![Matrices de Confusión por Modelo](../../data/results/confusion_matrices.png)

#### Clase 0 (Transacciones Legítimas)
- **Precision**: 1.00 (100%)
- **Recall**: 0.97 (97%)
- **Support**: 5,691 transacciones

#### Clase 1 (Transacciones Fraudulentas)
- **Precision**: 0.03 (3%)
- **Recall**: 1.00 (100%)
- **Support**: 5 transacciones

## Análisis de los Resultados

### Fortalezas del Modelo Baseline

1. **Alto Recall**: 100% de detección de transacciones fraudulentas
2. **Excelente AUC**: 0.9997 indica muy buena capacidad discriminativa
3. **Estabilidad**: Validación cruzada consistente (F1: 0.9524 ± 0.0005)
4. **Simplicidad**: Modelo lineal fácil de interpretar y desplegar

### Debilidades del Modelo Baseline

1. **Baja Precisión**: Solo 3% de precisión para transacciones fraudulentas
2. **F1-Score Limitado**: 0.0588 debido al desbalance de clases
3. **Falsos Positivos**: Alto número de transacciones legítimas marcadas como fraudulentas
4. **Linealidad**: Limitaciones para capturar relaciones no lineales complejas

### Comparación con Otros Modelos

![Comparación de Métricas por Modelo](../../data/results/metrics_comparison.png)

| Modelo | F1-Score | AUC | Ranking |
|--------|----------|-----|---------|
| Random Forest | 0.5000 | 0.9995 | **1º** |
| KNN | 0.1639 | 0.9972 | **2º** |
| Naive Bayes | 0.0709 | 0.9938 | **3º** |
| **Logistic Regression** | **0.0588** | **0.9997** | **4º** |
| Gradient Boosting | 0.0654 | 0.9966 | **5º** |
| Decision Tree | 0.0588 | 0.8382 | **6º** |

## Conclusiones

### Rendimiento del Baseline

El modelo baseline (Logistic Regression) establece una línea base sólida con:
- **AUC excelente** (0.9997) que indica buena capacidad discriminativa
- **Recall perfecto** (100%) para detección de fraude
- **Estabilidad** en validación cruzada

### Limitaciones Identificadas

1. **Desbalance de clases** afecta significativamente la precisión
2. **F1-Score bajo** (0.0588) debido a la baja precisión
3. **Modelo lineal** puede no capturar patrones complejos de fraude

### Áreas de Mejora

1. **Ajuste de umbrales**: Optimizar el punto de corte para balancear precisión y recall
2. **Feature engineering**: Crear características adicionales más discriminativas
3. **Técnicas de balanceo**: Probar diferentes métodos de balanceo de clases
4. **Modelos no lineales**: Evaluar modelos más complejos como Random Forest

### Validación del Enfoque

El modelo baseline confirma que:
- El problema es **técnicamente solucionable** (AUC > 0.99)
- Los **datos son informativos** para la detección de fraude
- Se requiere **optimización adicional** para mejorar la precisión

## Referencias

- Dataset: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Scikit-learn: Logistic Regression implementation
- SMOTE: Synthetic Minority Over-sampling Technique
- Métricas de evaluación: Precision, Recall, F1-Score, AUC-ROC

---

**Fecha de evaluación**: $(date)  
**Versión del baseline**: 1.0  
**Dataset**: 10% muestreado (5,696 transacciones)  
**Mejor métrica**: AUC = 0.9997
