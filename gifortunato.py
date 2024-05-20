import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Carregar o arquivo CSV
file_path = "archive.csv"  # Certifique-se de substituir "archive.csv" pelo nome do seu arquivo CSV
data = pd.read_csv(file_path)

# Exibir o dataframe (opcional)
st.write("Conteúdo do arquivo CSV:", data)

# Criar o gráfico
st.subheader("Gráfico a partir do conteúdo do arquivo CSV")
chart_type = st.selectbox("Selecione o tipo de gráfico:", ["Gráfico de Linhas", "Gráfico de Barras"])

if chart_type == "Gráfico de Linhas":
    st.line_chart(data)
elif chart_type == "Gráfico de Barras":
    st.bar_chart(data)

# Exemplo de outros tipos de gráficos que você pode criar:
# - st.area_chart(data) para gráfico de área
# - st.pyplot() para gráficos personalizados usando Matplotlib
