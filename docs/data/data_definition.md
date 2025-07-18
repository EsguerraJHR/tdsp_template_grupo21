# Definición de Datos - Credit Card Fraud Detection

## Descripción General del Dataset

El dataset contiene transacciones de tarjetas de crédito europeas realizadas en septiembre de 2013, donde se presentan transacciones fraudulentas y legítimas. Los datos han sido anonimizados para proteger la privacidad de los usuarios.

## Fuente de Datos

- **Origen:** Transacciones reales de tarjetas de crédito europeas
- **Período:** 03/05/2021
- **Plataforma:** Kaggle - Credit Card Fraud Detection
- **URL:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Estructura del Dataset

### Variables Originales
- **Time:** Tiempo transcurrido entre cada transacción y la primera transacción del dataset (en segundos)
- **Amount:** Monto de la transacción en euros
- **Class:** Variable objetivo (0 = transacción legítima, 1 = transacción fraudulenta)

### Variables Transformadas - Componentes principales obtenidos mediante PCA (Principal Component Analysis)
- **Propósito:** Preservar la privacidad de los datos originales
- **Características:** Variables numéricas estandarizadas que capturan patrones complejos

## Características Técnicas

### Dimensiones
- **Filas:** 284,807
- **Columnas:** 31 variables (28 transformadas + 2 originales + 1 objetivo)

### Distribución de Clases
- **Transacciones legítimas:** 284,315
- **Transacciones fraudulentas:** 492
- **Desbalance:** Extremo (ratio 1:577) 

### Calidad de Datos
- **Valores faltantes:** 0
- **Duplicados**: 0
- **0utliers:** Presentes en la variable Amount
- **Consistencia:** Excelente

## Preprocesamiento Aplicado

### 1 División de Datos
- **Train set:** 80 de los datos (227,845 transacciones)
- **Test set:** 20% de los datos (56,962 transacciones)
- **Estratificación:** Mantiene la proporción de clases en ambos sets

### 2. Estandarización
- **Método:** StandardScaler (Z-score normalization)
- **Aplicado a:** Todas las variables numéricas
- **Propósito:** Normalizar las escalas para algoritmos de ML

### 3. Balanceo de Clases
- **Método:** SMOTE (Synthetic Minority Over-sampling Technique)
- **Aplicado a:** Solo el set de entrenamiento
- **Resultado:** Clases balanceadas para evitar sesgo en el modelo

## Variables Más Importantes

### Top 5 Variables por Correlación con Fraude
1. **V17:** Correlación = 0.3265 (más importante)
2. **V14:** Correlación = 0.3253 
3. **V12:** Correlación = 0.2664
4. **V10:** Correlación = 0.21695
5. **V16:** Correlación = 00.1965

## Consideraciones para el Modelado

### Desafíos
1. **Desbalance extremo:** Requiere técnicas especiales de sampling
2. **Variables anónimas:** Limitación en interpretabilidad
3. **Outliers:** Presentes en montos de transacciones

### Ventajas
1. **Datos limpios:** Sin valores faltantes o duplicados
2. **Variables transformadas:** Optimizadas para ML.
3. **Dataset real:** Representativo de casos reales de fraude

## Archivos Generados

### Datos Procesados
- `X_train_balanced.csv`: Features de entrenamiento balanceadas
- `y_train_balanced.csv`: Target de entrenamiento balanceado
- `X_test_scaled.csv`: Features de test estandarizadas
- `y_test.csv`: Target de test original
- `scaler.pkl`: Modelo de estandarización guardado

### Documentación
- `data_dictionary.md`: Diccionario detallado de variables
- `data_summary.md`: Resumen estadístico y análisis
- `data_report.md`: Reporte exploratorio completo
- `creditcard_profile_report.html`: Reporte interactivo con ydata-profiling
