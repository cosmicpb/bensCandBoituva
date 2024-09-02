import pandas as pd

# Ler os arquivos CSV
df_candidatos = pd.read_csv('consulta_cand_2024_SP_Boituva.csv', delimiter=';', encoding='latin1')
df_bens = pd.read_csv('bens_candidatos_boituva.csv', delimiter=';', encoding='latin1')

# Converter a coluna de valores de bens para o tipo numérico, removendo possíveis símbolos de moeda
df_bens['VR_BEM_CANDIDATO'] = df_bens['VR_BEM_CANDIDATO'].replace({'R$': '', ',': '.'}, regex=True).astype(float)

# Calcular a soma do valor dos bens por candidato
df_soma_bens = df_bens.groupby('SQ_CANDIDATO')['VR_BEM_CANDIDATO'].sum().reset_index()
df_soma_bens.rename(columns={'VR_BEM_CANDIDATO': 'Total de Bens'}, inplace=True)

# Adicionar dados dos candidatos
df_completo = pd.merge(df_candidatos, df_soma_bens, on='SQ_CANDIDATO', how='left')

# Identificar candidatos sem bens
df_completo['Total de Bens'] = df_completo['Total de Bens'].fillna(0)

# Selecionar colunas de interesse
colunas_de_interesse = [
    'SQ_CANDIDATO', 'NM_CANDIDATO', 'NM_URNA_CANDIDATO', 'NM_SOCIAL_CANDIDATO', 'SG_PARTIDO', 
    'Total de Bens', 'DS_GENERO', 'DS_GRAU_INSTRUCAO', 'DS_COR_RACA', 'DS_OCUPACAO'
]
df_final = df_completo[colunas_de_interesse]

# Salvar o resultado em um novo arquivo CSV
df_final.to_csv('total/bens_candidatos_soma.csv', index=False, sep=';')
