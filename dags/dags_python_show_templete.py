from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task 

with DAG(
    dag_id="dags_python_show_templete",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=True
) as dag: 
    
    @task(task_id='python_task') 
    def show_templetes(**kwargs): 
        from pprint import pprint 
        pprint(kwargs)
            
    show_templetes()
    
    
    