from project.prefect_flow.flow import weather_etl


def create_deployment():
    weather_etl.deploy(
        name="weather-deployment",
        cron="* * * * *",
        work_pool_name="weather_deploy",
        image="weather-flow:latest"
    )