# main.py

# Instagram	 https://console.apify.com/actors/shu8hvrXbJbY3Eb9W/input
# facebook   https://console.apify.com/actors/KoJrdxJCTtpon81KY/input

from google_sheet import *
from send_to_bigquery import *
from datetime import datetime
from api_key import client
from constants import dia_atual,ontem, run
from midia_scraper import midia_sraper

dados_teste = dados_candidatos.iloc[0:2]

while run == True:
    midia_sraper(client, dados_teste, "instagram", data = "2024-10-08", daily = False)
    #midia_sraper(client, dados_teste, "facebook", data = "2024-09-20", daily = False)
    print("tempo final do script:", datetime.today())

    run = False
