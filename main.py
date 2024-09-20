
import pandas as pd
import time
from datetime import datetime
from datetime import timedelta, datetime
from apify_client import ApifyClient
from google_sheet import *
from functions import *

# Token Kaio  - apify_api_eJxbqPXXuzt9rP9aQQnQEprGsA24TE38w9ib
# Token ibpad - 

client = ApifyClient("apify_api_eJxbqPXXuzt9rP9aQQnQEprGsA24TE38w9ib")

insta_urls_test = insta_urls[0:2]
face_urls_test  = face_urls[0:2]

dia_atual = datetime.today()
x = dia_atual.weekday()

ontem = dia_atual - timedelta(days = 1)

df_final_insta = pd.DataFrame()
df_final_face = pd.DataFrame()

i = 0 

#run = True

print("tempo de inicio:", dia_atual)
print("raspando instagram...")

for url in insta_urls_test:
    i = i + 1

    #print(f"Scrapando dados para URL: {url}")

    run_input_insta = {
        "addParentData": False,
        "directUrls": [url],                         # Url do candidato
        "enhanceUserSearchWithFacebookPage": False,
        "isUserReelFeedURL": False,
        "isUserTaggedFeedURL": False,
        "resultsLimit": 3 if x != 0 else 6,          # N de resulados (caso for segunda 6 resultados)
        "resultsType": "posts",
        "searchLimit": 1
    }

    # Chamando a API e obtendo os resultados
    run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input = run_input_insta)

    # Iterando sobre os itens retornados pela API
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        post_date = item.get("timestamp")

        date_obj = datetime.strptime(post_date, '%Y-%m-%dT%H:%M:%S.%fZ')

        if x == 0:
            # teste pseudo retroativo segunda feira:
            #    objetivo - raspar dados do final de semana
            anteontem = ontem - timedelta(days = 1)

            if format_date(date_obj) == format_date(ontem) or format_date(date_obj) == format_date(anteontem):
                df_temp = pd.DataFrame([item])
                df_final_insta = pd.concat([df_final_insta, df_temp], ignore_index=True)

        if x != 0:
            if format_date(date_obj) == format_date(ontem):
                df_temp = pd.DataFrame([item])
                df_final_insta = pd.concat([df_final_insta, df_temp], ignore_index=True)

    time.sleep(5)
    
    # if i == 50:
    #     time.sleep(100)

    #     i = 0


print("raspando facebook...")

for url in face_urls_test:

    # Prepare the Actor input
    run_input_facebook = {
        "startUrls": [{ "url": url}],
        "resultsLimit": 2 if x != 0 else 4, 
    }

    run = client.actor("KoJrdxJCTtpon81KY").call(run_input = run_input_facebook)

    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        item.get("time")

        post_date = item.get("time")

        date_obj = datetime.strptime(post_date, '%Y-%m-%dT%H:%M:%S.%fZ')

        if x == 0:
            # teste pseudo retroativo segunda feira:
            #    objetivo - raspar dados do final de semana
            anteontem = ontem - timedelta(days = 1)

            if format_date(date_obj) == format_date(ontem) or format_date(date_obj) == format_date(anteontem):
                df_temp = pd.DataFrame([item])
                df_final_face = pd.concat([df_final_face, df_temp], ignore_index=True)

        if x != 0:

            if format_date(date_obj) == format_date(ontem):
                df_temp = pd.DataFrame([item])
                df_final_face = pd.concat([df_final_face, df_temp], ignore_index=True)

    time.sleep(5)

dia_atual2 = datetime.today()
print("tempo final do script:", dia_atual2)