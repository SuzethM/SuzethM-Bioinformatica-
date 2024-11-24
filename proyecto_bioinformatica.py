# -*- coding: utf-8 -*-
"""Proyecto Bioinformatica

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PAzs7bn5CwRw2MpK3U3Nb2T_1MnFMlVu
"""

# Instalar las dependencias necesarias en tu entorno
# Ejecuta en la terminal: pip install streamlit biopython

import streamlit as st
from Bio.Seq import Seq
from Bio.SeqUtils import seq3

# Función para procesar secuencias de ADN/ARN
def analyze_dna(sequence):
    sequence = Seq(sequence.strip().upper())
    if not all(base in "ACGTU" for base in sequence):
        return "**Error:** La secuencia contiene caracteres no válidos. Solo se permiten A, C, G, T, U."

    length = len(sequence)
    gc_content = 100 * (sequence.count("G") + sequence.count("C")) / length
    complement = sequence.complement()
    transcribed = sequence.transcribe() if "T" in sequence else "No aplica (ARN)"

    return f"""
    ### Resultados del análisis de ADN/ARN:
    - **Longitud de la secuencia:** {length} bases
    - **Contenido GC:** {gc_content:.2f}%
    - **Complemento:** {complement}
    - **Transcripción:** {transcribed}
    """

# Función para procesar secuencias de proteínas
def analyze_protein(sequence):
    sequence = Seq(sequence.strip().upper())
    if not all(residue in "ACDEFGHIKLMNPQRSTVWY" for residue in sequence):
        return "**Error:** La secuencia contiene caracteres no válidos. Usa el formato de una letra para aminoácidos."

    length = len(sequence)
    hydrophobic = sum(sequence.count(res) for res in "AILMFWV")
    hydrophilic = sum(sequence.count(res) for res in "RNDQEGKH")
    seq_three_letter = seq3(str(sequence))

    return f"""
    ### Resultados del análisis de proteínas:
    - **Longitud de la secuencia:** {length} aminoácidos
    - **Residuos hidrofóbicos:** {hydrophobic} ({100 * hydrophobic / length:.2f}%)
    - **Residuos hidrofílicos:** {hydrophilic} ({100 * hydrophilic / length:.2f}%)
    - **Secuencia en formato de tres letras:** {seq_three_letter}
    """

# Configuración de la interfaz en Streamlit
st.title("Análisis de Secuencias Biológicas")

# Selección del tipo de análisis
analysis_type = st.radio("Selecciona el tipo de análisis:", ["Análisis de ADN/ARN", "Análisis de Proteínas"])

# Entrada de la secuencia
sequence = st.text_area("Introduce la secuencia aquí:", height=150)

# Mostrar resultados al presionar el botón
if st.button("Analizar"):
    if analysis_type == "Análisis de ADN/ARN":
        result = analyze_dna(sequence)
        st.markdown(result)
    else:
        result = analyze_protein(sequence)
        st.markdown(result)

