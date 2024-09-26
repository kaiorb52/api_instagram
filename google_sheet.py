# google_sheet.py

import pandas as pd

def transformar_para_lista(valor):
    if valor == '-' or pd.isna(valor):
        return '-'
    return [url.strip() for url in valor.split(',')]

url = "https://docs.google.com/spreadsheets/d/1wK-eyn3xudbCbmpdwhh57z-RZvFAk-BRKktPjPLiPfI/export?format=csv&gid=445436196"

dados_candidatos = pd.read_csv(url)
#dados_candidatos = dados_candidatos.replace(['0', 0], None)

dados_candidatos['facebook_list']  = dados_candidatos['facebook'].apply(transformar_para_lista)
dados_candidatos['instagram_list'] = dados_candidatos['instagram'].apply(transformar_para_lista)
