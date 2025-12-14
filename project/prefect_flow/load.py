from prefect import task

from project.prefect_flow import clickhouse_client


@task
def load_hourly_data(hourly_data: list[dict]):
    for record in hourly_data:
        clickhouse_client.insert("weather_hourly", record)

@task
def load_daily_data(daily_data: dict):
    clickhouse_client.insert("weather_daily", daily_data)

@task
def load_alert_data(alert_data: dict):
    for record in alert_data:
        clickhouse_client.insert("alerts", record)