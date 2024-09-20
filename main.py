
import pandas as pd
import time
import datetime
from datetime import datetime
from apify_client import ApifyClient
from datetime import timedelta, datetime
import time
from google_sheet import *

insta_urls_test = insta_urls[0:2]

def format_date(date):
    return date.strftime('%Y-%m-%d')

# Token Kaio  - apify_api_eJxbqPXXuzt9rP9aQQnQEprGsA24TE38w9ib
# Token ibpad - 

client = ApifyClient("apify_api_eJxbqPXXuzt9rP9aQQnQEprGsA24TE38w9ib")

dia_atual = datetime.today()
ontem = dia_atual - timedelta(days=1)

df_final = pd.DataFrame()

i = 0 

#run = True

for url in insta_urls_test:
    i = i + 1
    print(f"Scrapando dados para URL: {url}")

    run_input = {
        "addParentData": False,
        "directUrls": [url],                         # Url do candidato
        "enhanceUserSearchWithFacebookPage": False,
        "isUserReelFeedURL": False,
        "isUserTaggedFeedURL": False,
        "resultsLimit": 3,                           # N de resulados
        "resultsType": "posts",
        "searchLimit": 1
    }

    # Chamando a API e obtendo os resultados
    run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

    # Iterando sobre os itens retornados pela API
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        post_date = item.get("timestamp")

        date_obj = datetime.datetime.strptime(post_date, '%Y-%m-%dT%H:%M:%S.%fZ')

        if format_date(date_obj) == format_date(ontem):
            print(1)

            df_temp = pd.DataFrame([item])
            
            df_final = pd.concat([df_final, df_temp], ignore_index=True)

    time.sleep(5)
    
    if i == 50:
        time.sleep(250)
        i = 0

