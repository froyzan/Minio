from minio import Minio
from minio.error import S3Error

# Создание клиента MinIO
client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False  # Установите в True, если используете HTTPS
)

try:
    # Получение списка корзин
    buckets = client.list_buckets() 
    if not buckets:
      print("Buckets list empty")
    else:
      for bucket in buckets:
        print(f"Bucket Name: {bucket.name}, Created On: {bucket.creation_date}")
except S3Error as e:
    print(f"Ошибка при получении списка корзин: {e}")
