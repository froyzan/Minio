from minio import Minio
from minio.error import S3Error
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False  # Установите в True, если используете HTTPS
)

bucket_name = "test-bucket"

# Проверка существования корзины и создание, если она не существует
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

def create_pdf(file_name, text):
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

# Создание и загрузка PDF-файлов
for i in range(1, 11):
    pdf_file_name = f"file_{i}.pdf"
    create_pdf(pdf_file_name, f"This is PDF file number {i}")

    # Загрузка файла в корзину MinIO
    try:
        with open(pdf_file_name, "rb") as file_data:
            client.put_object(bucket_name, pdf_file_name, file_data, os.path.getsize(pdf_file_name))
        print(f"{pdf_file_name} загружен в корзину {bucket_name}.")
    except S3Error as e:
        print(f"Ошибка при загрузке {pdf_file_name}: {e}")

    # Удаление локального файла после загрузки
    os.remove(pdf_file_name)

print("Все файлы успешно созданы и загружены.")
