from airflow import DAG
from datetime import timedelta

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

import urllib.request
import time
import glob, os
import json

def store_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('wrote file: ' + file)

def catalog():

    def pull(url):
        try:
            response = urllib.request.urlopen(url).read()
            data = response.decode('utf-8')
            return data
        except urllib.error.HTTPError as e:
            if e.code == 404:  # If the error is a 404, print and skip
                print(f"HTTPError 404 for URL: {url} - Page not found. Skipping...")
                return None  # Return None to signal failure
            else:
                # For other HTTP errors, log the error and return None
                print(f"HTTPError for URL: {url} - {e.code} {e.reason}")
                return None
        except urllib.error.URLError as e:
            print(f"URLError for URL: {url} - {e.reason}. Skipping...")
            return None  # Return None for URL errors
        except Exception as e:
            print(f"Unexpected error for URL: {url} - {str(e)}. Skipping...")
            return None  # Catch any other unexpected exceptions

    def store(data, file):
        if data:  # Only store data if it is not None
            with open(file, 'w') as out:
                out.write(data)
                print(f'Wrote file: {file}')
        else:
            print(f"Skipping {file} due to missing data.")

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

def combine():

    with open('combo.txt', 'w') as outfile:
        for file in glob.glob('*.html'):
            with open(file, 'r') as infile:
                outfile.write(infile.read())

def titles():
    from bs4 import BeautifulSoup

    with open('combo.txt','r') as infile:
        html = infile.read()

        html = html.replace('\n', ' ').replace('\r', '')
        # the following create an html parser
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all('h3')
        titles = []

        # tag inner text
        for item in results:
            titles.append(item.text)
        store_json(titles, 'titles.json')

def clean():

   with open('titles.json') as file:
       titles = json.load(file)
       # remove punctuation/numbers
       for index, title in enumerate(titles):
           punctuation= '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
           translationTable= str.maketrans("","",punctuation)
           clean = title.translate(translationTable)
           titles[index] = clean

       # remove one character words
       for index, title in enumerate(titles):
           clean = ' '.join( [word for word in title.split() if len(word)>1] )
           titles[index] = clean

       store_json(titles, 'titles_clean.json')

def count_words():
    from collections import Counter
    with open('titles_clean.json') as file:
        titles = json.load(file)
        words = []

        # extract words and flatten
        for title in titles:
            words.extend(title.split())

        # count word frequency
        counts = Counter(words)
        store_json(counts, 'words.json')

with DAG(
   "assignment",
   start_date=days_ago(1),
   schedule_interval="@daily",
   catchup=False,
) as dag:
    # INSTALL BS4 BY HAND THEN CALL FUNCTION

    # ts are tasks
    t0 = BashOperator(
        task_id='task_zero',
        bash_command='pip install beautifulsoup4',
        retries=2
    )
    t1 = PythonOperator(
        task_id='task_one',
        depends_on_past=False,
        python_callable=catalog
    )
    t2 = PythonOperator(
        task_id='task_two',
        depends_on_past=False,
        python_callable=combine
    )
    t3 = PythonOperator(
        task_id='task_three',
        depends_on_past=False,
        python_callable=titles
    )
    t4 = PythonOperator(
        task_id='task_four',
        depends_on_past=False,
        python_callable=clean
    )
    t5 = PythonOperator(
        task_id='task_five',
        depends_on_past=False,
        python_callable=count_words
    )

    # Task Dependencies (execution order)
    t0 >> t1 >> t2 >> t3 >> t4 >> t5

#catalog()
#combine()
#titles()
#clean()
#count_words()
