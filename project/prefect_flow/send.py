
import requests
from prefect import task

from project.prefect_flow import *


@task(retries=3, retry_delay_seconds=15)
def send_message(normalize_daily_data, normalize_alerts_data, city, tomorrow_date):
    try:
        message = f"Прогноз погоды на {tomorrow_date} для города {city}\n 🌡 Min temp: {normalize_daily_data['min_temp_c']:.1f}°C\n 🌡 Max temp: {normalize_daily_data['max_temp_c']:.1f}°C\n 🌧 Осадки: {normalize_daily_data['precipitation_mm']:.1f} мм\n"
        if len(normalize_alerts_data) != 0:
            message += "Внимание!"
            for alert in normalize_alerts_data:
                message += f"\n⚠️ {alert['headline']}. {alert['message']}"
        tg_client.send(message)
    except Exception as e:
        print(f"Ошибка отправки данных в телеграм для {city}: {e}")
        raise e
