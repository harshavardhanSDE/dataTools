from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 8),
    'retries': 1,
}

def ingest() -> dict:
    import requests
    import json 

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

def format(res) -> dict:
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['phone'] = res['phone']
    data['email'] = res['email']
    data['address'] = f"{location['street']['number']}, {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['username'] = res['login']['username']
    data['password'] = res['login']['password']
    data['dob'] = res['dob']['date']
    data['registered'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data


def stream_data():
    import requests
    import json 

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    print(json.dumps(res, indent=4))

# with DAG('kafka', default_args=default_args, schedule_interval='@daily',catchup=False) as dag:
#     stream_data = PythonOperator(
#         task_id='stream_data',
#         python_callable=stream_data
#     )

stream_data()
print(format(ingest()))    
