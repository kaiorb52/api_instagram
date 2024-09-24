# midia_scraper.py

import pandas as pd
import time
from datetime import datetime
from datetime import timedelta, datetime
from constants import dia_atual,ontem, run, x
from functions import format_date

def midia_sraper(client, urls, midia, inicio):
  
  df_final = pd.DataFrame()
  inicio   = datetime.today()
  i        = 0
  
  print("tempo de inicio:", inicio)
  print(f"raspando {midia}...")
  
  if midia == "instagram":
    n_post     = 5
    n_weekends = n_post * 2
    api        = "shu8hvrXbJbY3Eb9W"
    time_var   = "timestamp"
  
  if midia == "facebook":
    n_post     = 2
    n_weekends = n_post * 2
    api        = "KoJrdxJCTtpon81KY"
    time_var   = "time"
  
  for url in urls:
      i = i + 1

      if midia == "instagram":
        run_input = {
            "addParentData": False,
            "directUrls": [url],                              # Url do candidato
            "enhanceUserSearchWithFacebookPage": False,
            "isUserReelFeedURL": False,
            "isUserTaggedFeedURL": False,
            "onlyPostsNewerThan": "2024-09-01",
            "resultsLimit": n_post if x != 0 else n_weekends, # N de resulados (caso for segunda 6 resultados)
            "resultsType": "posts",
            "searchLimit": 1
        }

      if midia == "facebook":
        run_input = {
          "startUrls": [{ "url": url}],
          "resultsLimit": n_post if x != 0 else n_weekends, 
        }

      # Chamando a API e obtendo os resultados
      run = client.actor(api).call(run_input = run_input)

      # Iterando sobre os itens retornados pela API
      for item in client.dataset(run["defaultDatasetId"]).iterate_items():
          post_date = item.get(time_var)
          date_obj  = datetime.strptime(post_date, '%Y-%m-%dT%H:%M:%S.%fZ')
          df_temp   = pd.DataFrame()
          
          df_temp = pd.DataFrame([item])

          df_final = pd.concat([df_final, df_temp], ignore_index=True)
          
      time.sleep(1)
      
      if i == 50:
        i = 0
        time.sleep(500)
        
  df_final.to_csv(f'data/{midia}_{inicio}.csv', index=False)
  print("tempo final do script:", datetime.today())

