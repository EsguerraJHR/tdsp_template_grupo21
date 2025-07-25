"""
Fase 3: Modelado y Extracción de Características
Entrena y evalúa múltiples modelos de clasificación para detección de fraude.
Versión optimizada con validación cruzada eficiente.
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_auc_score, 
    precision_recall_curve, roc_curve, accuracy_score, precision_score,
    recall_score, f1_score
)
from sklearn.model_selection import cross_val_score, StratifiedKFold
import warnings

import joblib

warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
RESULTS_DIR = 'data/results'
os.makedirs(RESULTS_DIR, exist_ok=True)

def load_processed_data(sample_size=0.1, random_state=42):
    """
    Carga datos procesados con sampling opcional para evitar problemas de memoria
    Args:
        sample_size: Porcentaje del dataset a usar (0.1 = 10%)
        random_state: Semilla para reproducibilidad
    """
    try:
        X_train = pd.read_csv('data/processed/X_train_balanced.csv')
        y_train = pd.read_csv('data/processed/y_train_balanced.csv')
        X_test = pd.read_csv('data/processed/X_test_scaled.csv')
        y_test = pd.read_csv('data/processed/y_test.csv')
        
        if isinstance(y_train, pd.DataFrame):
            y_train = y_train.values.ravel()
        if isinstance(y_test, pd.DataFrame):
            y_test = y_test.values.ravel()
        
        print(f"Dataset original - Train: {X_train.shape}, Test: {X_test.shape}")
        
        # Aplicar sampling si se especifica
        if sample_size < 1.0:
            # Calcular número de muestras para train
            n_train_samples = int(len(X_train) * sample_size)
            # Calcular número de muestras para test (mantener proporción)
            n_test_samples = int(len(X_test) * sample_size)
            
            # Sampling estratificado para train
            from sklearn.model_selection import train_test_split
            X_train_sampled, _, y_train_sampled, _ = train_test_split(
                X_train, y_train, 
                train_size=n_train_samples, 
                stratify=y_train, 
                random_state=random_state
            )
            
            # Sampling simple para test
            X_test_sampled = X_test.sample(n=n_test_samples, random_state=random_state)
            y_test_sampled = y_test[X_test_sampled.index]
            
            print(f"Dataset muestreado ({sample_size*100}%) - Train: {X_train_sampled.shape}, Test: {X_test_sampled.shape}")
            print(f"Distribución de clases en train: {np.bincount(y_train_sampled)}")
            print(f"Distribución de clases en test: {np.bincount(y_test_sampled)}")
            
            return X_train_sampled, y_train_sampled, X_test_sampled, y_test_sampled
        else:
            print(f"Usando dataset completo")
            return X_train, y_train, X_test, y_test
            
    except FileNotFoundError:
        print("Error: Datos procesados no encontrados. Ejecuta primero el preprocesamiento.")
        return None, None, None, None

def define_models():
    """Define modelos optimizados para velocidad con dataset pequeño"""
    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=300),
        'Random Forest': RandomForestClassifier(n_estimators=30, random_state=42, n_jobs=-1),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=30, random_state=42),
        'KNN': KNeighborsClassifier(n_neighbors=3, n_jobs=-1),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=10),
        'Naive Bayes': GaussianNB()
    }
    return models

def train_and_evaluate_models(X_train, y_train, X_test, y_test):
    models = define_models()
    results = {}
    
    # Configuración de validación cruzada (reducida para velocidad)
    cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
    
    print("Entrenando modelos con validación cruzada...")
    for name, model in models.items():
        print(f"Entrenando {name}...")
        
        # Validación cruzada para métricas robustas
        cv_scores_f1 = cross_val_score(model, X_train, y_train, cv=cv, scoring='f1', n_jobs=-1)
        cv_scores_auc = cross_val_score(model, X_train, y_train, cv=cv, scoring='roc_auc', n_jobs=-1)
        
        # Entrenamiento final en todo el conjunto de entrenamiento
        model.fit(X_train, y_train)
        
        # Predicciones en test
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
        
        # Métricas en test
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred_proba) if y_pred_proba is not None else None
        
        results[name] = {
            'model': model,
            'y_pred': y_pred,
            'y_pred_proba': y_pred_proba,
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'auc': auc,
            'cv_f1_mean': cv_scores_f1.mean(),
            'cv_f1_std': cv_scores_f1.std(),
            'cv_auc_mean': cv_scores_auc.mean(),
            'cv_auc_std': cv_scores_auc.std()
        }
        
        print(f"  Test F1: {f1:.4f}, Test AUC: {auc:.4f}" if auc else f"  Test F1: {f1:.4f}")
        print(f"  CV F1: {cv_scores_f1.mean():.4f} ± {cv_scores_f1.std():.4f}")
        print(f"  CV AUC: {cv_scores_auc.mean():.4f} ± {cv_scores_auc.std():.4f}")
    
    return results

def plot_confusion_matrices(results, y_test):
    n_models = len(results)
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.ravel()
    for i, (name, result) in enumerate(results.items()):
        cm = confusion_matrix(y_test, result['y_pred'])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[i])
        axes[i].set_title(f'{name}\nConfusion Matrix')
        axes[i].set_xlabel('Predicted')
        axes[i].set_ylabel('Actual')
    for i in range(n_models, len(axes)):
        axes[i].set_visible(False)
    plt.tight_layout()
    plt.savefig(f'{RESULTS_DIR}/confusion_matrices.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_roc_curves(results, y_test):
    plt.figure(figsize=(12, 8))
    for name, result in results.items():
        if result['y_pred_proba'] is not None:
            fpr, tpr, _ = roc_curve(y_test, result['y_pred_proba'])
            auc = result['auc']
            plt.plot(fpr, tpr, label=f'{name} (AUC = {auc:.3f})')
    plt.plot([0, 1], [0, 1], '--', label='Random')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{RESULTS_DIR}/roc_curves.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_precision_recall_curves(results, y_test):
    plt.figure(figsize=(12, 8))
    for name, result in results.items():
        if result['y_pred_proba'] is not None:
            precision, recall, _ = precision_recall_curve(y_test, result['y_pred_proba'])
            plt.plot(recall, precision, label=f'{name}')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curves Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{RESULTS_DIR}/precision_recall_curves.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_metrics_comparison(results):
    metrics = ['accuracy', 'precision', 'recall', 'f1']
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.ravel()
    for i, metric in enumerate(metrics):
        values = [results[name][metric] for name in results.keys()]
        names = list(results.keys())
        bars = axes[i].bar(names, values)
        axes[i].set_title(f'{metric.capitalize()} Comparison')
        axes[i].set_ylabel(metric.capitalize())
        axes[i].tick_params(axis='x', rotation=45)
        for bar, value in zip(bars, values):
            axes[i].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                        f'{value:.3f}', ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig(f'{RESULTS_DIR}/metrics_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_feature_importance(results, X_train):
    importance_models = ['Random Forest', 'Gradient Boosting', 'Decision Tree']
    available_models = [name for name in importance_models if name in results]
    
    if not available_models:
        print("No hay modelos con importancia de características disponibles")
        return
    
    fig, axes = plt.subplots(1, len(available_models), figsize=(6*len(available_models), 6))
    if len(available_models) == 1:
        axes = [axes]
    
    for i, name in enumerate(available_models):
        model = results[name]['model']
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
            indices = np.argsort(importances)[::-1]
            top_features = indices[:10]
            top_importances = importances[top_features]
            feature_names = [X_train.columns[j] for j in top_features]
            axes[i].barh(range(len(top_importances)), top_importances)
            axes[i].set_yticks(range(len(top_importances)))
            axes[i].set_yticklabels(feature_names)
            axes[i].set_xlabel('Importance')
            axes[i].set_title(f'{name} - Top 10 Features')
            axes[i].invert_yaxis()
    
    plt.tight_layout()
    plt.savefig(f'{RESULTS_DIR}/feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()

def save_results_to_csv(results):
    results_data = []
    for name, result in results.items():
        results_data.append({
            'Model': name,
            'Test_Accuracy': result['accuracy'],
            'Test_Precision': result['precision'],
            'Test_Recall': result['recall'],
            'Test_F1-Score': result['f1'],
            'Test_AUC': result['auc'],
            'CV_F1_Mean': result['cv_f1_mean'],
            'CV_F1_Std': result['cv_f1_std'],
            'CV_AUC_Mean': result['cv_auc_mean'],
            'CV_AUC_Std': result['cv_auc_std']
        })
    df_results = pd.DataFrame(results_data)
    df_results = df_results.sort_values('Test_F1-Score', ascending=False)
    df_results.to_csv(f'{RESULTS_DIR}/model_results.csv', index=False)
    print("\nResultados guardados en model_results.csv:")
    print(df_results.to_string(index=False))
    return df_results

def generate_classification_reports(results, y_test):
    with open(f'{RESULTS_DIR}/classification_reports.txt', 'w') as f:
        for name, result in results.items():
            f.write(f"\n{'='*50}\n")
            f.write(f"CLASSIFICATION REPORT - {name}\n")
            f.write(f"{'='*50}\n")
            f.write(classification_report(y_test, result['y_pred']))
            if result['auc'] is not None:
                f.write(f"\nAUC Score: {result['auc']:.4f}\n")
    print("\nReportes de clasificación guardados en classification_reports.txt")

def save_best_model(results, output_path='scripts/deployment/best_model.joblib'):
    """
    Guarda el mejor modelo (según F1 en test) usando joblib
    """
    best_model_name = max(results, key=lambda name: results[name]['f1'])
    best_model = results[best_model_name]['model']
    joblib.dump(best_model, output_path)
    print(f"\n✅ Modelo '{best_model_name}' guardado en {output_path}")

def main():
    print("=== FASE 3 MODELADO Y EXTRACCIÓN DE CARACTERÍSTICAS ===\n")
    print("Usando 10% del dataset para evitar problemas de memoria...")
    X_train, y_train, X_test, y_test = load_processed_data(sample_size=0.1, random_state=42)
    if X_train is None:
        return
    results = train_and_evaluate_models(X_train, y_train, X_test, y_test)
    print("\nGenerando visualizaciones...")
    plot_confusion_matrices(results, y_test)
    plot_roc_curves(results, y_test)
    plot_precision_recall_curves(results, y_test)
    plot_metrics_comparison(results)
    plot_feature_importance(results, X_train)
    print("\nGuardando resultados...")
    save_results_to_csv(results)
    generate_classification_reports(results, y_test)
    save_best_model(results)
    print(f"Todos los resultados guardados en {RESULTS_DIR}/")
    print("Gráficas generadas:")
    print("  - confusion_matrices.png")
    print("  - roc_curves.png")
    print("  - precision_recall_curves.png")
    print("  - metrics_comparison.png")
    print("  - feature_importance.png")
    print("📄 Archivos de datos:")
    print("  - model_results.csv")
    print("  - classification_reports.txt")

if __name__ == "__main__":
    main() 