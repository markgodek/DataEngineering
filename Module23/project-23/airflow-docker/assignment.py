from airflow import DAG
from datetime import timedelta

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

import urllib.request
import time
import glob, os
import json

def catalog():

    def pull(url):
        response = urllib.request.urlopen(url).read()
        data = response.decode('utf-8')
        return data

    def store(data,file):
        with open(file, 'w') as out:
            out.write(data)
            print('wrote file: ' + file)

    urls = [
        "http://student.mit.edu/catalog/m1a.html",
        "http://student.mit.edu/catalog/m1b.html",
        "http://student.mit.edu/catalog/m1c.html",
        "http://student.mit.edu/catalog/m2a.html",
        "http://student.mit.edu/catalog/m2b.html",
        "http://student.mit.edu/catalog/m2c.html",
        "http://student.mit.edu/catalog/m3a.html",
        "http://student.mit.edu/catalog/m3b.html",
        "http://student.mit.edu/catalog/m4a.html",
        "http://student.mit.edu/catalog/m4b.html",
        "http://student.mit.edu/catalog/m4c.html",
        "http://student.mit.edu/catalog/m4d.html",
        "http://student.mit.edu/catalog/m4e.html",
        "http://student.mit.edu/catalog/m4f.html",
        "http://student.mit.edu/catalog/m4g.html",
        "http://student.mit.edu/catalog/m5a.html",
        "http://student.mit.edu/catalog/m5b.html",
        "http://student.mit.edu/catalog/m6a.html",
        "http://student.mit.edu/catalog/m6b.html",
        "http://student.mit.edu/catalog/m6c.html",
        "http://student.mit.edu/catalog/m7a.html",
        "http://student.mit.edu/catalog/m8a.html",
        "http://student.mit.edu/catalog/m8b.html",
        "http://student.mit.edu/catalog/m9a.html",
        "http://student.mit.edu/catalog/m9b.html",
        "http://student.mit.edu/catalog/m10a.html",
        "http://student.mit.edu/catalog/m10b.html",
        "http://student.mit.edu/catalog/m10c.html",
        "http://student.mit.edu/catalog/m11a.html",
        "http://student.mit.edu/catalog/m11b.html",
        "http://student.mit.edu/catalog/m11c.html",
        "http://student.mit.edu/catalog/m12a.html",
        "http://student.mit.edu/catalog/m12b.html",
        "http://student.mit.edu/catalog/m12c.html",
        "http://student.mit.edu/catalog/m14a.html",
        "http://student.mit.edu/catalog/m14b.html",
        "http://student.mit.edu/catalog/m15a.html",
        "http://student.mit.edu/catalog/m15b.html",
        "http://student.mit.edu/catalog/m15c.html",
        "http://student.mit.edu/catalog/m16a.html",
        "http://student.mit.edu/catalog/m16b.html",
        "http://student.mit.edu/catalog/m18a.html",
        "http://student.mit.edu/catalog/m18b.html",
        "http://student.mit.edu/catalog/m20a.html",
        "http://student.mit.edu/catalog/m22a.html",
        "http://student.mit.edu/catalog/m22b.html",
        "http://student.mit.edu/catalog/m22c.html"
    ]

    for url in urls:
        data = pull(url)
        print('pulled: ' + url)
        print('--- waiting ---')
        time.sleep(15)

        # get the index of the character after the last slash and
        # use everything after as the file name for use by the store function
        index = url.rfind('/') + 1
        file = url[index:]
        print(file)
        store(data, file)

catalog()

# step 5 here
#https://classroom.emeritus.org/courses/9296/assignments/218600?module_item_id=1556656