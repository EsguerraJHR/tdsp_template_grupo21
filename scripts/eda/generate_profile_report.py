import pandas as pd
from ydata_profiling import ProfileReport
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_PATH / 'data' / 'raw' / 'creditcard.csv'
OUTPUT_PATH = BASE_PATH / 'outputs' / 'creditcard_profile_report.html'

df = pd.read_csv(DATA_PATH)
profile = ProfileReport(df, title='Credit Card Fraud Detection - Data Profile', explorative=True)
profile.to_file(OUTPUT_PATH)
print(f'Reporte HTML generado en {OUTPUT_PATH}') 