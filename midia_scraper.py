# midia_scraper.py

import pandas as pd
import time
import os
from datetime import timedelta, datetime
from constants import dia_atual,ontem, run
from functions import format_date


def midia_sraper(
  client, 
  df, 
  midia, 
  data = (datetime.today() - timedelta(days = 1)).strftime("%Y-%m-%d"), 
  daily = True):
    
  midia_var  = midia + '_list'
  dados      = df[midia_var]
  df_perma   = pd.DataFrame()
  inicio     = datetime.today()
  dia_semana = dia_atual.weekday()
  i          = 0
  
  print("post de antes de:", data)
  print("tempo de inicio:", inicio)
  print(f"raspando {midia}...")
  
  if midia == "instagram":
    n_post     = 300
    api        = "shu8hvrXbJbY3Eb9W"
    time_var   = "timestamp"
  
  if midia == "facebook":
    n_post     = 200
    api        = "KoJrdxJCTtpon81KY"
    time_var   = "time"
  
  if daily == True and dia_semana == 0:
    data = (datetime.today() - timedelta(days = 2)).strftime("%Y-%m-%d") 
    
  for idx, candidato in enumerate(dados):
    #for candidato in dados:
    candidato_id = df.loc[idx, 'ID']
    for url in candidato:
      i = i + 1

      if midia == "instagram":
        run_input = {
            "addParentData": False,
            "directUrls": [url],              # Url do candidato
            "enhanceUserSearchWithFacebookPage": False,
            "isUserReelFeedURL": False,
            "isUserTaggedFeedURL": False,
            "onlyPostsNewerThan": data,       # >= data
            "resultsLimit": n_post,           # N de resulados
            "resultsType": "posts",
            "searchLimit": 1
        }
        colunas = [
          'CandidatoID',                      # Variavel utilizada para o join no final do script
          'inputUrl', 'id', 'type', 'shortCode', 'caption', 'url',
          'commentsCount', 'likesCount', 'videoViewCount', 'videoPlayCount',
          'timestamp', 'ownerFullName', 'ownerUsername', 'ownerId'
        ]


      if midia == "facebook":
        run_input = {
          "startUrls": [{ "url": url}],       # Url do candidato
          "onlyPostsNewerThan": data,         # >= data
          "resultsLimit": n_post,             # N de resulados
        }
        colunas = [
          'CandidatoID'
        ]

      
      # Chamando a API e obtendo os resultados
      run = client.actor(api).call(run_input = run_input)

      # Iterando sobre os itens retornados pela API
      for item in client.dataset(run["defaultDatasetId"]).iterate_items():

          df_temp  = pd.DataFrame(columns=colunas)
          df_temp  = pd.DataFrame([item])
          df_temp['CandidatoID'] = candidato_id

          df_perma = pd.concat([df_perma, df_temp], ignore_index=True)
          
      time.sleep(2)
      
      if i == 50:
        i = 0
        time.sleep(100)
      
  results   = df_perma[colunas]
  
  results_f = pd.merge(
    df,             
    results,                
    left_on    = 'ID',
    right_on   = 'CandidatoID',  
    how        = 'left'      
  )
          
  # credentials = service_account.Credentials.from_service_account_file('bq_auth.json')

  # project_id = 'uc3m-autoridades'
  # dataset_id = 'monitoramento'
  # table_name = 'prefeitos_scrapper_facebook'
  # path = f'{project_id}.{dataset_id}.{table_name}'

  # upload_bigquery(credentials, project_id, path, results_final, 'overwrite')
  
  # if ('data' in os.listdir()) == False:
  #  os.mkdir('data')
  # results_f.to_csv(f'data/{midia}_{inicio}.csv', index=False)

  print(f"tempo final da raspasgem do {midia}:", datetime.today())

