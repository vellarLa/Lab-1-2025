FROM prefecthq/prefect:3.6.6-python3.11
COPY requirements.txt /opt/prefect/Lab-1-2025/requirements.txt
RUN uv pip install -r /opt/prefect/Lab-1-2025/requirements.txt
COPY . /opt/prefect/Lab-1-2025/
WORKDIR /opt/prefect/Lab-1-2025/
