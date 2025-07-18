import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from pathlib import Path
import pickle

# Paths
BASE_PATH = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_PATH / 'data' / 'raw' / 'creditcard.csv'
PROCESSED_PATH = BASE_PATH / 'data' / 'processed'
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

print("Cargando datos...")
df = pd.read_csv(DATA_PATH)

print("Información inicial del dataset:")
print(f"- Shape: {df.shape}")
print(f"- Distribución de clases: {df['Class'].value_counts().to_dict()}")

# Separar features y target
X = df.drop('Class', axis=1)
y = df['Class']

# Dividir en train/test (estratificado)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTrain set: {X_train.shape[0]} muestras")
print(f"Test set: {X_test.shape[0]} muestras")

# Estandarizar variables numéricas
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convertir de vuelta a DataFrame
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

print("\nVariables estandarizadas")

# Aplicar SMOTE para balancear las clases
print("Aplicando SMOTE para balancear clases...")
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_scaled, y_train)

print(f"Distribución después de SMOTE: {pd.Series(y_train_balanced).value_counts().to_dict()}")

# Guardar datos procesados
print("Guardando datos procesados...")
X_train_balanced.to_csv(PROCESSED_PATH / 'X_train_balanced.csv', index=False)
y_train_balanced.to_csv(PROCESSED_PATH / 'y_train_balanced.csv', index=False)
X_test_scaled.to_csv(PROCESSED_PATH / 'X_test_scaled.csv', index=False)
y_test.to_csv(PROCESSED_PATH / 'y_test.csv', index=False)

# Guardar scaler
with open(PROCESSED_PATH / 'scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Preprocesamiento completado!")
print(f"Datos guardados en: {PROCESSED_PATH}") 