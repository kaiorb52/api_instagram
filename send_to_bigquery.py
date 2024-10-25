from google.cloud import bigquery
from google.oauth2 import service_account

# credentials = service_account.Credentials.from_service_account_file('path.json')
# client = bigquery.Client(credentials=credentials, project=credentials.project_id)

def send_to_bigquery(df, table_id):
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,  
        autodetect=True,  
    )

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()

    table = client.get_table(table_id)
    print(f"Carregado {table.num_rows} linhas para a tabela {table_id}.")
