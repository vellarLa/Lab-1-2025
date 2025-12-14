from dotenv import load_dotenv
import os
from project.clickhouse_bd.clickhouse_client import ClickhouseClient
from project.minio_client.minio_client import MinioClient
from project.telegram.telegram_client import TelegramClient

load_dotenv()
API_KEY = os.getenv('API_KEY')

tg_client = TelegramClient()
minio_client = MinioClient()
clickhouse_client = ClickhouseClient()

CITIES = {
    "Moscow": {"lat": 55.7558, "lon": 37.6173},
    "Samara": {"lat": 53.1951, "lon": 50.1067}
}