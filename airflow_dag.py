# airflow_dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import trade_executor

def execute_trade():
    trade_executor.execute_trade()

def monitor_trade():
    trade_executor.monitor_trades()

def alert_trade():
    trade_executor.alert_on_trade()

def create_dag():
    dag = DAG(
        "trade_execution_pipeline",
        default_args={"start_date": datetime(2024, 1, 1)},
        schedule_interval="@hourly",
    )

    execute = PythonOperator(
        task_id="execute_trade",
        python_callable=execute_trade,
        dag=dag,
    )
    monitor = PythonOperator(
        task_id="monitor_trade",
        python_callable=monitor_trade,
        dag=dag,
    )
    alert = PythonOperator(
        task_id="alert_trade",
        python_callable=alert_trade,
        dag=dag,
    )
    
    execute >> monitor >> alert
    
    return dag

dag = create_dag()
