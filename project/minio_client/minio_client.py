from minio import Minio
from project.minio_client import *
import io


class MinioClient:
    def __init__(self):
        self.client = Minio(MINIO_ENDPOINT, MINIO_ROOT_USER, MINIO_ROOT_PASSWORD, secure=False)
        if not self.client.bucket_exists(MINIO_BUCKET_NAME):
            self.client.make_bucket(MINIO_BUCKET_NAME)

    def put(self, filename: str, raw_data: str):
        self.client.put_object(
            MINIO_BUCKET_NAME,
            filename,
            data=io.BytesIO(bytes(raw_data, 'utf-8')),
            length=len(raw_data),
            content_type='application/json'
        )
