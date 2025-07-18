import pandas as pd
from pathlib import Path

# Paths
BASE_PATH = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_PATH / 'data' / 'raw' / 'creditcard.csv'
OUTPUT_PATH = BASE_PATH / 'docs' / 'data' / 'data_summary.md'

df = pd.read_csv(DATA_PATH)

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write('# Resumen de datos\n\n')
    f.write(f'- **Número de filas:** {df.shape[0]}\n')
    f.write(f'- **Número de columnas:** {df.shape[1]}\n')
    f.write('- **Variables:** ' + ', '.join(df.columns) + '\n\n')
    f.write('## Valores nulos por columna\n')
    f.write(df.isnull().sum().to_string())
    f.write('\n\n')
    f.write('## Estadísticas descriptivas principales\n')
    f.write(df.describe().to_markdown())
print(f'Resumen de datos generado en {OUTPUT_PATH}') 