# google_sheet.py

import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1wK-eyn3xudbCbmpdwhh57z-RZvFAk-BRKktPjPLiPfI/export?format=csv&gid=0"

dados_candidatos = pd.read_csv(url)

insta_urls = dados_candidatos["Instagram_0"]
face_urls = dados_candidatos["Facebook_0"]
