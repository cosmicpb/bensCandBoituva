import pandas as pd

# Tentar ler os arquivos com a codificação correta
try:
    df_candidatos = pd.read_csv('consulta_cand_2024_SP_Boituva.csv', delimiter=';', encoding='latin1')
    df_bens = pd.read_csv('bem_candidato_2024_SP.csv', delimiter=';', encoding='latin1')
except Exception as e:
    print(f"Erro ao ler os arquivos CSV: {e}")

# Cruzar os dados utilizando a coluna SQ_CANDIDATO como chave
df_bens_boituva = pd.merge(df_candidatos, df_bens, on='SQ_CANDIDATO')

# Ajustar a lista de colunas de interesse
colunas_de_interesse = [
    'SQ_CANDIDATO', 'NM_CANDIDATO', 'NM_UE_x', 'DS_CARGO', 'SG_PARTIDO',
    'DS_TIPO_BEM_CANDIDATO', 'DS_BEM_CANDIDATO', 'VR_BEM_CANDIDATO'
]

# Selecionar apenas as colunas de interesse
df_bens_boituva = df_bens_boituva[colunas_de_interesse]

# Salvar o resultado em um novo arquivo CSV
df_bens_boituva.to_csv('bens_candidatos_boituva.csv', index=False, sep=';')
