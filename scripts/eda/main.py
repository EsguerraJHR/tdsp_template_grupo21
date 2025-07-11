#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_datos(path):
    if not os.path.exists(path):
        print(f"❌ ERROR: No se encuentra el archivo {path}")
        return None
    print(f"📂 Cargando datos desde: {path}")
    return pd.read_csv(path)

def resumen_general(df):
    print("\n=== RESUMEN GENERAL DE LOS DATOS ===")
    print(f"🔢 Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    print("\n📋 Tipos de datos:")
    print(df.dtypes)
    print("\n🧪 Valores faltantes por columna:")
    print(df.isnull().sum())
    print("\n🔍 Valores únicos por columna:")
    print(df.nunique())

def vista_por_tipo(df):
    if 'tipo_declaracion' in df.columns:
        print("\n=== FORMULARIOS PRESENTES ===")
        print(df['tipo_declaracion'].value_counts())
        print("\n=== VISTA DETALLADA POR FORMULARIO ===")
        for tipo in df['tipo_declaracion'].unique():
            print(f"\n📄 {tipo.upper()}:\n")
            print(df[df['tipo_declaracion'] == tipo].T)

def estadisticas_monetarias(df):
    print("\n=== ESTADÍSTICAS DE VARIABLES MONETARIAS ===")
    columnas_monetarias = [col for col in df.columns if "valor" in col.lower() or "monto" in col.lower() or "saldo" in col.lower()]
    for col in columnas_monetarias:
        print(f"\n💰 {col}:")
        print(df[col].describe())
        if df.shape[0] > 1:
            sns.histplot(df[col].dropna(), bins=10, kde=True)
            plt.title(f"Distribución de {col}")
            plt.tight_layout()
            plt.savefig(f"outputs/eda/hist_{col}.png")
            plt.close()

def generar_matriz_correlacion(df):
    columnas_numericas = df.select_dtypes(include=["int64", "float64"]).columns
    if len(columnas_numericas) > 1:
        print("\n=== MATRIZ DE CORRELACIÓN ===")
        corr = df[columnas_numericas].corr()
        print(corr)
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Matriz de correlación")
        plt.tight_layout()
        plt.savefig("outputs/eda/matriz_correlacion.png")
        plt.close()

def main():
    ruta_entrada = "data/processed/declaraciones_consolidadas.csv"
    os.makedirs("outputs/eda", exist_ok=True)

    df = cargar_datos(ruta_entrada)
    if df is None:
        return

    resumen_general(df)
    vista_por_tipo(df)
    estadisticas_monetarias(df)
    generar_matriz_correlacion(df)

    print("\n✅ EDA básico completado. Resultados guardados en: outputs/eda/")

if __name__ == "__main__":
    main()