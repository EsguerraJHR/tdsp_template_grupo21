import pandas as pd
from pathlib import Path

# Paths
BASE_PATH = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_PATH / 'data' / 'raw' / 'creditcard.csv'
OUTPUT_PATH = BASE_PATH / 'docs' / 'data' / 'data_dictionary.md'

df = pd.read_csv(DATA_PATH)

# Diccionario de datos
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write('# Diccionario de datos\n\n')
    f.write('| Variable | Descripción | Tipo de dato | Ejemplo |\n')
    f.write('|---|---|---|---|\n')
    for col in df.columns:
        tipo = str(df[col].dtype)
        ejemplo = df[col].dropna().iloc[0] if not df[col].dropna().empty else ''
        if col == 'Time':
            desc = 'Tiempo transcurrido desde la primera transacción en el dataset (segundos)'
        elif col == 'Amount':
            desc = 'Monto de la transacción'
        elif col == 'Class':
            desc = 'Clase objetivo: 0 = No Fraude, 1 = Fraude'
        else:
            desc = 'Variable anónima transformada (PCA): ' + col
        f.write(f'| {col} | {desc} | {tipo} | {ejemplo} |\n')
print(f'Diccionario de datos generado en {OUTPUT_PATH}') 