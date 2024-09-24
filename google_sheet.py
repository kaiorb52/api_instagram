# google_sheet.py

import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1wK-eyn3xudbCbmpdwhh57z-RZvFAk-BRKktPjPLiPfI/export?format=csv&gid=0"

dados_candidatos = pd.read_csv(url)
dados_candidatos = dados_candidatos.replace(['0', 0], None)

def unificar_redes_sociais(df, prefixo):
    colunas_redes = [col for col in df.columns if col.startswith(prefixo)]
    
    redes_candidatos = []
    for i, row in df.iterrows():
        redes_individuais = []
        for col in colunas_redes:
            if pd.notna(row[col]):
                redes_individuais.append(row[col])
        redes_candidatos.append(redes_individuais)
    
    return redes_candidatos

# Coletando todas as redes sociais (Instagram e Facebook neste caso)
instagram_candidatos = unificar_redes_sociais(dados_candidatos, 'Instagram')
facebook_candidatos  = unificar_redes_sociais(dados_candidatos, 'Facebook')

instagram_test = instagram_candidatos[0:2]
facebook_test  = facebook_candidatos[0:2]

  # i = 0
  # for candidato in instagram_candidatos:
  #   for url in candidato:
  #     i = i + 1
  #     print(url)
  #     print(i)
  # 
  # i = 0
  # for candidato in facebook_candidatos:
  #   for url in candidato:
  #     i = i + 1
  #     print(url)
  #     print(i)
