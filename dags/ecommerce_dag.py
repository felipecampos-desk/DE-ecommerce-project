import os
from datetime import timedelta, datetime
from dotenv import load_dotenv
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Armezenar variaveis de ambientes
SCRIPTS_PATH = os.getenv("SCRIPTS_PATH")
DBT_DIR = os.getenv("DBT_DIR")

# Criando função para gerar dados fakes
def generate_data():
    os.system(f"python {SCRIPTS_PATH}generate_fake_data.py")


default_args = {
    'owner': 'Felipe',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    dag_id= "ecommerce_analytics_dag",
    default_args= default_args,
    start_date= datetime(2025, 8, 2),
    schedule= "@weekly",
    catchup= False,
    tags= ["ecommerce", "analytics", "dbt", "churn"]
) as dag:
    # Inserindo as tarefas na Dag (task)
    
    # Task 1: gerar os dados fakes
    t1_generate_data= PythonOperator(
        task_id= "generate_fake_data",
        python_callable= generate_data
    )

    # Task 2: executar o dbt seed
    t2_dbt_seed = BashOperator(
        task_id= "dbt_seed",
        bash_command= f"cd {DBT_DIR} && dbt seed --profiles-dir /usr/local/airflow/include/.dbt"
    )

    # Task 3: executar o dbt run
    t3_dbt_run = BashOperator(
        task_id= "dbt_run",
        bash_command= f"cd {DBT_DIR} && dbt run --profiles-dir /usr/local/airflow/include/.dbt"
    )

    # Task 4: executar o dbt test
    t4_dbt_test = BashOperator(
        task_id= "dbt_test",
        bash_command= f"cd {DBT_DIR} && dbt test --profiles-dir /usr/local/airflow/include/.dbt"
    )

    # Task 5: gerar o relatório
    t5_generate_report = BashOperator(
        task_id= "generate_report",
        bash_command= f"python {os.path.join(SCRIPTS_PATH, 'generate_report.py')}"
    )

    # Definir a ordem de execução das tasks(tarefas da Dag)
    t1_generate_data >> t2_dbt_seed >> t3_dbt_run >> t4_dbt_test >> t5_generate_report