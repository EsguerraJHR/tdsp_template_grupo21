#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.diagnostico_tributario.procesador import procesar_un_pdf
import pandas as pd
import glob
from pathlib import Path

def main():
    """
    Script principal para procesar todas las declaraciones tributarias
    """
    print("=== PROCESAMIENTO DE DECLARACIONES TRIBUTARIAS ===")
    print("Usando extracción directa de PDF para análisis de datos")
    
    # Directorio de PDFs de entrada
    directorio_pdfs = "data/raw/declaraciones_pdf"
    
    # Verificar que existe el directorio
    if not os.path.exists(directorio_pdfs):
        print(f"❌ ERROR: No se encontró el directorio {directorio_pdfs}")
        return
    
    # Buscar todos los PDFs
    patron_busqueda = os.path.join(directorio_pdfs, "*.pdf")
    archivos_pdf = glob.glob(patron_busqueda)
    
    if not archivos_pdf:
        print(f"❌ ERROR: No se encontraron archivos PDF en {directorio_pdfs}")
        return
    
    print(f"📄 Encontrados {len(archivos_pdf)} archivos PDF:")
    for pdf in archivos_pdf:
        print(f"  - {os.path.basename(pdf)}")
    
    # Procesar cada PDF
    dataframes_resultados = []
    
    for pdf_path in archivos_pdf:
        print(f"\n🔄 Procesando {os.path.basename(pdf_path)}...")
        try:
            df_resultado = procesar_un_pdf(pdf_path)
            dataframes_resultados.append(df_resultado)
            print(f"  ✅ Procesado exitosamente")
        except Exception as e:
            print(f"  ❌ Error al procesar {pdf_path}: {e}")
            continue
    
    # Consolidar resultados
    if dataframes_resultados:
        df_consolidado = pd.concat(dataframes_resultados, ignore_index=True)
        
        # Guardar resultado consolidado
        archivo_salida = "data/processed/declaraciones_consolidadas.csv"
        os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)
        df_consolidado.to_csv(archivo_salida, index=False)
        
        print(f"\n📊 RESUMEN DE PROCESAMIENTO:")
        print(f"  Total archivos procesados: {len(dataframes_resultados)}")
        print(f"  Registros consolidados: {len(df_consolidado)}")
        print(f"  Archivo de salida: {archivo_salida}")
        
        # Mostrar vista previa de los datos
        print(f"\n📋 VISTA PREVIA DE DATOS:")
        columnas_vista = ['fuente_pdf', 'tipo_declaracion', 'valores_encontrados', 'valor_maximo', 'metodo_extraccion']
        print(df_consolidado[columnas_vista].to_string(index=False))
        
        print(f"\n✅ Procesamiento completado exitosamente!")
        print(f"💾 Datos guardados en: {archivo_salida}")
    else:
        print(f"\n❌ No se pudo procesar ningún archivo PDF")

if __name__ == "__main__":
    main()
