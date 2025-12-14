import pendulum
from prefect import flow

from project.prefect_flow import CITIES
from project.prefect_flow.extract import extract_weather_data, save_raw_data_to_s3
from project.prefect_flow.send import send_message
from project.prefect_flow.transform import transform_weather_hourly, transform_weather_daily, transform_weather_alerts
from project.prefect_flow.load import load_hourly_data, load_daily_data, load_alert_data


@flow(name="weather_etl")
def weather_etl():
    for city in CITIES:
        tomorrow_date = pendulum.tomorrow('Europe/Moscow').format('YYYY-MM-DD')
        # Этап EXTRACT
        response = extract_weather_data(city)
        save_raw_data_to_s3(response.text, city)
        # Этап TRANSFORM
        normalize_hourly_data = transform_weather_hourly(response.json(), city, tomorrow_date)
        normalize_daily_data = transform_weather_daily(response.json(), city, tomorrow_date)
        normalize_alerts_data = transform_weather_alerts(response.json(), city, tomorrow_date)
        # Этап LOAD
        load_hourly_data(normalize_hourly_data)
        load_daily_data(normalize_daily_data)
        load_alert_data(normalize_alerts_data)
        # Этап SEND
        send_message(normalize_daily_data, normalize_alerts_data, city, tomorrow_date)






