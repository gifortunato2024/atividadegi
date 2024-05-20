import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Carregar o arquivo CSV
file_path = "archive.csv"  
data = pd.read_csv(file_path)

# Exibir o dataframe (opcional)
st.write("Conteúdo do arquivo CSV:", data)

# Criar o gráfico de barras
st.subheader("Gráfico de Barras a partir do conteúdo do arquivo CSV")
st.bar_chart(data)
