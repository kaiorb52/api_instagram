from google.cloud import bigquery
from google.oauth2 import service_account

def upload_bigquery(credentials, project_id, path, df, modo_carregamento=None):
    try:
        job_config = bigquery.LoadJobConfig()
        job_config.autodetect = False
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND if modo_carregamento == 'append' else bigquery.WriteDisposition.WRITE_TRUNCATE

        client = bigquery.Client(credentials=credentials, project=project_id)
        load_job = client.load_table_from_dataframe(df, path, job_config=job_config)
        load_job.result()  # Espera o job finalizar

        print("Upload para o BigQuery realizado com sucesso.")

    except Exception as e:
        print(f"Erro ao fazer upload para o BigQuery: {e}")


# Exemplo de uso:
# credentials = service_account.Credentials.from_service_account_file('path/to/credentials.json')
# upload_bigquery(credentials, 'meu_projeto', 'meu_dataset', 'minha_tabela', df, 'append')