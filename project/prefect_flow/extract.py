from datetime import datetime

import requests
from prefect import task
from requests import Response

from project.prefect_flow import *


@task(retries=3, retry_delay_seconds=15)
def extract_weather_data(city: str) -> Response:
    try:
        api_url = f'http://api.weatherapi.com/v1/forecast.json?q={city}&days=2&aqi=no&alerts=yes&key={API_KEY}'
        response = requests.get(api_url)
        if response.status_code != 200:
            raise Exception(response.text)
        return response
    except Exception as e:
        print(f"Ошибка получения данных для {city}: {e}")
        raise e


@task(retries=3, retry_delay_seconds=15)
def save_raw_data_to_s3(raw_json: str, city: str):
    try:
        filename = f"{city}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        minio_client.put(filename, raw_json)
    except Exception as e:
        print(f"Ошибка сохранения сырых данных в объектное хранилище: {e}")
        raise e
