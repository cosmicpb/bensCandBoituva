import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('bens_candidatos_soma.csv', delimiter=';')

# Configuração da página
st.title("Bens dos Candidatos a Vereador em Boituva - SP")
st.write("Eleições Municipais 2024")
st.write("Por Paulo Baldacim e João Baldacim")

# Gráfico dos 20 candidatos mais ricos
st.header("Top 20 Candidatos Mais Ricos")
top_20_candidatos = df.nlargest(20, 'Total de Bens')
fig, ax = plt.subplots(figsize=(10, 8))
sns.barplot(x='Total de Bens', y='NM_CANDIDATO', data=top_20_candidatos, palette='viridis', ax=ax)
ax.set_xlabel('Total de Bens (R$)')
ax.set_ylabel('Nome do Candidato')
ax.set_title('Top 20 Candidatos Mais Ricos')
st.pyplot(fig)

# Distribuição de renda por gênero
st.header("Distribuição de Renda por Gênero")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='DS_GENERO', y='Total de Bens', data=df, ax=ax)
ax.set_xlabel('Gênero')
ax.set_ylabel('Total de Bens (R$)')
ax.set_title('Distribuição de Renda por Gênero')
st.pyplot(fig)

# Distribuição de renda por formação
st.header("Distribuição de Renda por Formação")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='DS_GRAU_INSTRUCAO', y='Total de Bens', data=df, ax=ax)
ax.set_xlabel('Formação')
ax.set_ylabel('Total de Bens (R$)')
ax.set_title('Distribuição de Renda por Formação')
st.pyplot(fig)

# Distribuição de renda por partido
st.header("Distribuição de Renda por Partido")
fig, ax = plt.subplots(figsize=(10, 8))
sns.boxplot(x='SG_PARTIDO', y='Total de Bens', data=df, ax=ax)
ax.set_xlabel('Partido')
ax.set_ylabel('Total de Bens (R$)')
ax.set_title('Distribuição de Renda por Partido')
plt.xticks(rotation=90)
st.pyplot(fig)

# Distribuição de renda por classe social (ocupação)
st.header("Distribuição de Renda por Ocupação")
fig, ax = plt.subplots(figsize=(10, 8))
sns.boxplot(x='DS_OCUPACAO', y='Total de Bens', data=df, ax=ax)
ax.set_xlabel('Ocupação')
ax.set_ylabel('Total de Bens (R$)')
ax.set_title('Distribuição de Renda por Ocupação')
plt.xticks(rotation=90)
st.pyplot(fig)
