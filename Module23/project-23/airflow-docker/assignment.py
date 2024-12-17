from airflow import DAG
from datetime import timedelta

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

import urllib.request
import time
import glob, os
import json

