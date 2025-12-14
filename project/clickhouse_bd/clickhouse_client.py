import  clickhouse_connect
from project.clickhouse_bd import *


class ClickhouseClient:
    def __init__(self):
        self.client = clickhouse_connect.get_client(host=CLICKHOUSE_HOST, port=CLICKHOUSE_PORT, username=CLICKHOUSE_USERNAME,
                             password=CLICKHOUSE_PASSWORD, database=CLICKHOUSE_DATABASE, secure=False)
    def insert(self, tablename: str, data):
        self.client.insert(tablename, [tuple(data.values())])
