import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
import pathlib
BASE_PATH = pathlib.Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_PATH / 'data' / 'raw' / 'creditcard.csv'
FIGURES_PATH = BASE_PATH / 'outputs' / 'figures'
OUTPUTS_PATH = BASE_PATH / 'outputs'
FIGURES_PATH.mkdir(parents=True, exist_ok=True)
OUTPUTS_PATH.mkdir(parents=True, exist_ok=True)

# Cargar datos
df = pd.read_csv(DATA_PATH)

# Estadísticas descriptivas
desc = df.describe()
desc.to_csv(OUTPUTS_PATH / 'creditcard_describe.csv')

# Distribución de la variable objetivo
plt.figure(figsize=(6,4))
sns.countplot(x='Class', data=df)
plt.title('Distribución de la variable objetivo (Class)')
plt.savefig(FIGURES_PATH / 'target_distribution.png')
plt.close()

# Histograma de montos
plt.figure(figsize=(6,4))
sns.histplot(df['Amount'], bins=50, kde=True)
plt.title('Distribución del monto de transacción')
plt.savefig(FIGURES_PATH / 'amount_distribution.png')
plt.close()

# Correlación de variables principales
corr = df.corr()
plt.figure(figsize=(12,10))
sns.heatmap(corr, cmap='coolwarm', center=0)
plt.title('Matriz de correlación')
plt.savefig(FIGURES_PATH / 'correlation_matrix.png')
plt.close()

# Boxplot de Amount por clase
plt.figure(figsize=(6,4))
sns.boxplot(x='Class', y='Amount', data=df)
plt.title('Boxplot de Amount por clase')
plt.savefig(FIGURES_PATH / 'amount_boxplot_by_class.png')
plt.close()

print('Imágenes y estadísticas guardadas en outputs/figures y outputs/') 