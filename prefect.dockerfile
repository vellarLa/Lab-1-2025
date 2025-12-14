FROM python:3.11

RUN pip install --upgrade pip
RUN pip install \
    prefect \
    clickhouse-driver \
    minio_client= \
    requests

WORKDIR /project