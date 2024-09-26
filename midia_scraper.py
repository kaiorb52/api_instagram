# midia_scraper.py

import pandas as pd
import time
import os
from datetime import datetime
from datetime import timedelta, datetime
from constants import dia_atual,ontem, run
from functions import format_date


def midia_sraper(client, dados, midia, 
  data = (datetime.today() - timedelta(days = 1)).strftime("%Y-%m-%d"), daily = True):
  
  df_final   = pd.DataFrame()
  inicio     = datetime.today()
  dia_semana = dia_atual.weekday()
  i          = 0
  
  print("post de antes de:", data)
  print("tempo de inicio:", inicio)
  print(f"raspando {midia}...")
  
  if midia == "instagram":
    n_post     = 300
    #n_weekends = n_post * 2
    api        = "shu8hvrXbJbY3Eb9W"
    time_var   = "timestamp"
  
  if midia == "facebook":
    n_post     = 200
    #n_weekends = n_post * 2
    api        = "KoJrdxJCTtpon81KY"
    time_var   = "time"
  
  if daily == True and dia_semana == 0:
    data = (datetime.today() - timedelta(days = 2)).strftime("%Y-%m-%d") 
  
  for candidato in dados:
    for url in candidato:
      i = i + 1
      print(i)
      print(url)
    
      if midia == "instagram":
        run_input = {
            "addParentData": False,
            "directUrls": [url],                        # Url do candidato
            "enhanceUserSearchWithFacebookPage": False,
            "isUserReelFeedURL": False,
            "isUserTaggedFeedURL": False,
            "onlyPostsNewerThan": data,                 # >= data
            "resultsLimit": n_post,                     # N de resulados
            "resultsType": "posts",
            "searchLimit": 1
        }

      if midia == "facebook":
        run_input = {
          "startUrls": [{ "url": url}],
          "onlyPostsNewerThan": data,
          "resultsLimit": n_post, 
        }

      # Chamando a API e obtendo os resultados
      run = client.actor(api).call(run_input = run_input)

      # Iterando sobre os itens retornados pela API
      for item in client.dataset(run["defaultDatasetId"]).iterate_items():
          # post_date = item.get(time_var)
          # date_obj  = datetime.strptime(post_date, '%Y-%m-%dT%H:%M:%S.%fZ')
          
          df_temp  = pd.DataFrame()
          df_temp  = pd.DataFrame([item])

          df_final = pd.concat([df_final, df_temp], ignore_index=True)
          
      time.sleep(1)
      
      # if i == 50:
      #   i = 0
      #   time.sleep(500)
  
  dirs = os.listdir()
  
  if ('data' in dirs) == False:
    os.mkdir('data')
    
  df_final.to_csv(f'data/{midia}_{inicio}.csv', index=False)
  print("tempo final do script:", datetime.today())

