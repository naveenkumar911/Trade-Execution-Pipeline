# README.md
# Automated Trade Execution Pipeline

## Overview
This project automates trade execution using Airflow, monitors trades, and sends alerts via Alpaca API.

## Features
- Airflow-based trade execution pipeline
- Automated order execution and monitoring
- Alert system for trade updates

## Installation
```sh
pip install -r requirements.txt
```

## Usage
Ensure Airflow is running and execute the DAG:
```sh
airflow dags trigger trade_execution_pipeline
```

---
