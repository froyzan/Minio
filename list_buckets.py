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
    # print(dir(client))
    buckets = client.list_buckets() 
    if not buckets:
      print("Buckets list empty")
    else:
      for bucket in buckets:
        print(f"Bucket Name: {bucket.name}, Created On: {bucket.creation_date}")
        objects = client.list_objects(bucket.name)
        found_objects = False
        for obj in objects:
          print(f"    - {obj.object_name} (Размер: {obj.size} байт)")
          found_objects = True  

        if not found_objects:
          print("    Нет файлов в этой корзине.")
except S3Error as e:
    print(f"Ошибка при получении списка корзин: {e}")
