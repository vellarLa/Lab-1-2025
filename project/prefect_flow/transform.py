from datetime import datetime, date

from prefect import task



@task
def transform_weather_hourly(data: dict, city: str, tomorrow_date):
    try:
        normalize_data = []
        forecastday_data: dict = data["forecast"]["forecastday"]
        for forecastday in forecastday_data:
            if forecastday["date"] != tomorrow_date:
                continue
            for hour_data in forecastday["hour"]:
                normalize_data.append({
                    "city": city,
                    "temp_c": hour_data["temp_c"],
                    "wind_speed_kph": hour_data["wind_kph"],
                    "wind_direction": hour_data["wind_dir"],
                    "chance_of_rain": hour_data["chance_of_rain"],
                    "chance_of_snow": hour_data["chance_of_snow"],
                    "precipitation_mm": hour_data["precip_mm"],
                    "time": datetime.strptime(hour_data["time"], "%Y-%m-%d %H:%M")
                })
        return normalize_data
    except Exception as e:
        print(f"Ошибка преобразования почасовых данных: {e}")
        raise e

@task
def transform_weather_daily(data: dict, city: str, tomorrow_date):
    try:
        forecastday_data: dict = data["forecast"]["forecastday"]
        for forecastday in forecastday_data:
            if forecastday["date"] != tomorrow_date:
                continue
            date_stat: dict = forecastday["day"]
            return {
                    "city": city,
                    "min_temp_c": date_stat["mintemp_c"],
                    "max_temp_c": date_stat["maxtemp_c"],
                    "avg_temp_c": date_stat["avgtemp_c"],
                    "precipitation_mm": date_stat["totalprecip_mm"],
                    "date": date.fromisoformat(tomorrow_date)
                }
    except Exception as e:
        print(f"Ошибка преобразования почасовых данных: {e}")
        raise e

@task
def transform_weather_alerts(data: dict, city: str, tomorrow_date):
    try:
        alerts = {}
        alert_data: dict = data["alerts"]["alert"]
        for alert in alert_data:
            alerts[alert["headline"]] ={
                "city": city,
                "headline": alert["headline"],
                "message": alert["desc"],
                "category": alert["event"],
                "instruction": alert["instruction"],
                "date": date.fromisoformat(tomorrow_date)
            }
        return alerts.values()
    except Exception as e:
        print(f"Ошибка преобразования почасовых данных: {e}")
        raise e