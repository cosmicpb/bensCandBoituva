import pandas as pd

# Ler o arquivo CSV original
df = pd.read_csv('consulta_cand_2024_SP.csv', delimiter=';')

# Filtrar os candidatos cuja cidade (NM_UE) é "BOITUVA"
df_boituva = df[df['NM_UE'] == 'BOITUVA']

# Salvar o novo DataFrame filtrado em um novo arquivo CSV
df_boituva.to_csv('consulta_cand_2024_SP_Boituva.csv', index=False, sep=';')
