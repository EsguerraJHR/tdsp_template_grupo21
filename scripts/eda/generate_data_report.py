import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier

# Paths
BASE_PATH = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_PATH / 'data' / 'raw' / 'creditcard.csv'
FIGURES_PATH = BASE_PATH / 'outputs' / 'figures'
REPORT_PATH = BASE_PATH / 'docs' / 'data' / 'data_report.md'
FIGURES_PATH.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    f.write('# Reporte de Datos\n\n')
    f.write('Este documento contiene los resultados del análisis exploratorio de datos.\n\n')

    # Resumen general
    f.write('## Resumen general de los datos\n\n')
    f.write(f'- **Número de filas:** {df.shape[0]}\n')
    f.write(f'- **Número de columnas:** {df.shape[1]}\n')
    f.write(f'- **Variables:** {', '.join(df.columns)}\n')
    f.write(f'- **Tipos de variables:** {df.dtypes.value_counts().to_dict()}\n')
    f.write(f'- **Valores faltantes:** {df.isnull().sum().sum()}\n')
    f.write(f'- **Duplicados:** {df.duplicated().sum()}\n')
    f.write('\n')

    # Resumen de calidad de los datos
    f.write('## Resumen de calidad de los datos\n\n')
    nulls = df.isnull().sum()
    nulls_percent = (nulls / len(df) * 100).round(2)
    f.write('### Valores faltantes por columna\n')
    f.write((nulls[nulls > 0].to_string() if nulls.sum() > 0 else 'No hay valores faltantes.') + '\n\n')
    f.write('### Porcentaje de valores faltantes por columna\n')
    f.write((nulls_percent[nulls_percent > 0].to_string() if nulls_percent.sum() > 0 else 'No hay valores faltantes.') + '\n\n')
    f.write(f'- **Duplicados:** {df.duplicated().sum()}\n')
    # Outliers (usando Amount)
    q1 = df['Amount'].quantile(0.25)
    q3 = df['Amount'].quantile(0.75)
    iqr = q3 - q1
    outliers = ((df['Amount'] < (q1 - 1.5 * iqr)) | (df['Amount'] > (q3 + 1.5 * iqr))).sum()
    f.write(f'- **Outliers en Amount:** {outliers}\n')
    f.write('\n')

    # Variable objetivo
    f.write('## Variable objetivo\n\n')
    f.write('Distribución de la variable objetivo (`Class`):\n')
    plt.figure(figsize=(6,4))
    sns.countplot(x='Class', data=df)
    plt.title('Distribución de la variable objetivo (Class)')
    plt.savefig(FIGURES_PATH / 'target_distribution.png')
    plt.close()
    f.write('![](../../outputs/figures/target_distribution.png)\n\n')
    f.write(df['Class'].value_counts(normalize=True).to_frame('proporcion').to_markdown() + '\n\n')

    # Variables individuales
    f.write('## Variables individuales\n\n')
    for col in df.columns:
        f.write(f'### {col}\n')
        f.write(f'- Tipo: {df[col].dtype}\n')
        f.write(f'- Valores únicos: {df[col].nunique()}\n')
        f.write(f'- Estadísticas:\n')
        f.write(df[col].describe().to_string() + '\n')
        if col not in ['Class']:
            # Histograma
            plt.figure(figsize=(6,4))
            sns.histplot(df[col], bins=50, kde=True)
            plt.title(f'Distribución de {col}')
            plt.savefig(FIGURES_PATH / f'{col}_hist.png')
            plt.close()
            f.write(f'![](../../outputs/figures/{col}_hist.png)\n')
            # Boxplot vs Class si es numérica
            if np.issubdtype(df[col].dtype, np.number):
                plt.figure(figsize=(6,4))
                sns.boxplot(x='Class', y=col, data=df)
                plt.title(f'Boxplot de {col} por clase')
                plt.savefig(FIGURES_PATH / f'{col}_box_by_class.png')
                plt.close()
                f.write(f'![](../../outputs/figures/{col}_box_by_class.png)\n')
        f.write('\n')

    # Ranking de variables (correlación y feature importance)
    f.write('## Ranking de variables\n\n')
    corr = df.corr()['Class'].abs().sort_values(ascending=False)
    f.write('### Correlación absoluta con la variable objetivo\n')
    f.write(corr.to_markdown() + '\n\n')
    # Feature importance con RandomForest
    X = df.drop('Class', axis=1)
    y = df['Class']
    rf = RandomForestClassifier(n_estimators=50, n_jobs=-1, random_state=42)
    rf.fit(X, y)
    importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
    f.write('### Importancia de variables (RandomForest)\n')
    f.write(importances.to_markdown() + '\n\n')

    # Relación entre variables explicativas y variable objetivo
    f.write('## Relación entre variables explicativas y variable objetivo\n\n')
    plt.figure(figsize=(12,10))
    sns.heatmap(df.corr(), cmap='coolwarm', center=0)
    plt.title('Matriz de correlación')
    plt.savefig(FIGURES_PATH / 'correlation_matrix.png')
    plt.close()
    f.write('![](../../outputs/figures/correlation_matrix.png)\n\n')

print(f'Reporte de datos generado en {REPORT_PATH}') 