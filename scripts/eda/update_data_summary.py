import pandas as pd
import numpy as np
from pathlib import Path

# Paths
BASE_PATH = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_PATH / data / 'raw' /creditcard.csv'
SUMMARY_PATH = BASE_PATH /docs /data' / 'data_summary.md'

df = pd.read_csv(DATA_PATH)

# Análisis del dataset
total_transactions = len(df)
fraud_transactions = df[Class].sum()
fraud_percentage = (fraud_transactions / total_transactions) * 10null_count = df.isnull().sum().sum()
duplicate_count = df.duplicated().sum()

# Análisis de outliers en Amount
q1 = df[Amount].quantile(0.25q3 = df[Amount].quantile(0.75
iqr = q3 - q1utliers_count = ((dfAmount] < (q1 -10.5qr)) | (dfAmount] > (q3 + 1.5 * iqr))).sum()

# Correlaciones más importantes con Class
correlations = df.corr()['Class'].abs().sort_values(ascending=False)
top_correlations = correlations.head(10)

with open(SUMMARY_PATH, w, encoding=utf-8') as f:
    f.write('# Resumen de Datos - Credit Card Fraud Detection\n\n')
    
    f.write('## Información General del Dataset\n\n)    f.write(f'- **Total de transacciones:** {total_transactions:,}\n)    f.write(f- **Transacciones fraudulentas:** {fraud_transactions:,} ({fraud_percentage:.2f}%)\n)    f.write(f- **Transacciones legítimas:** {total_transactions - fraud_transactions:,} ({100fraud_percentage:.2f}%)\n)    f.write(f'- **Número de variables:** [object Object]len(df.columns)}\n)    f.write(f- **Variables numéricas:** {len(df.select_dtypes(include=[np.number]).columns)}\n\n')
    
    f.write(##Calidad de los Datos\n\n)    f.write(f'- **Valores faltantes:** {null_count}\n)    f.write(f'- **Registros duplicados:** [object Object]duplicate_count}\n)    f.write(f'- **Outliers en Amount:** {outliers_count:,} ({outliers_count/total_transactions*100:0.2}%)\n\n')
    
    f.write('## Características del Dataset\n\n')
    f.write('- **Desbalance severo:** El dataset presenta un desbalance extremo con solo0.17% de transacciones fraudulentas\n')
    f.write('- **Variables anónimas:** 28 variables han sido transformadas usando PCA para preservar la privacidad\n')
    f.write('- **Variables originales:** Time (tiempo desde la primera transacción) y Amount (monto de la transacción)\n')
    f.write('- **Variable objetivo:** Class (0o Fraude, 1=Fraude)\n\n')
    
    f.write('## Variables Más Importantes\n\n')
    f.write('### Top 10 variables con mayor correlación absoluta con la variable objetivo:\n')
    for var, corr in top_correlations.items():
        if var != 'Class':
            f.write(f- **{var}:** {corr:.4f}\n)    f.write('\n')
    
    f.write('## Insights Principales\n\n')
    f.write(### 1. Desbalance de Clases\n')
    f.write('- El dataset presenta un desbalance extremo que requerirá técnicas especiales de sampling\n')
    f.write(- Las métricas de evaluación deberán considerar precision, recall y F1-score\n\n')
    
    f.write('### 2stribución de Montos\n')
    f.write('- La mayoría de las transacciones tienen montos bajos\n')
    f.write('- Existen outliers significativos en la variable Amount\n')
    f.write('- Las transacciones fraudulentas tienden a tener montos diferentes a las legítimas\n\n')
    
    f.write('### 3. Variables Transformadas\n')
    f.write('- Las28riables V1-V28n resultado de PCA, manteniendo la privacidad\n')
    f.write(- Estas variables capturan patrones complejos en los datos originales\n')
    f.write('- Algunas variables muestran correlaciones significativas con el fraude\n\n')
    
    f.write('## Recomendaciones para el Modelado\n\n)    f.write('1. **Técnicas de Sampling:** Usar SMOTE, undersampling o técnicas de ensemble para manejar el desbalance\n)    f.write('2. **Métricas de Evaluación:** Priorizar recall sobre accuracy debido al desbalance\n)    f.write('3. **Feature Engineering:** Considerar crear features basadas en Amount y Time\n)    f.write('4**Validación:** Usar stratified k-fold cross-validation\n)    f.write('5*Algoritmos:** Probar Random Forest, XGBoost, y técnicas de ensemble\n\n')
    
    f.write(## Reporte Detallado\n\n')
    f.write('Para un análisis exploratorio completo e interactivo, consulta el reporte HTML generado:\n')
    f.write('[Credit Card Fraud Detection - Data Profile](../../outputs/creditcard_profile_report.html)\n\n')
    
    f.write(Este reporte incluye:\n')
    f.write(-Análisis detallado de cada variable\n')
    f.write('- Matriz de correlación interactiva\n')
    f.write('- Distribuciones y estadísticas descriptivas\n')
    f.write('- Alertas de calidad de datos\n')
    f.write(- Recomendaciones automáticas\n')

print(f'Resumen de datos actualizado en {SUMMARY_PATH}') 