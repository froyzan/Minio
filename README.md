# FastAPI MinIO File Storage

![Minio Console](minio.jpg) <!-- Замените на путь к вашему изображению -->

Это приложение на FastAPI позволяет загружать и скачивать PDF-файлы в локальное хранилище MinIO. 

## Особенности

- Загрузка PDF-файлов в корзину `pdf_files`.
- Скачивание PDF-файлов из корзины.
- Получение списка файлов в корзине с информацией о каждом файле.

## Установка

1. Установка и запуск Minio
  ```bash
  git clone https://github.com/froyzan/Minio.git
  cd Minio
  chmod +x setup_minio.sh
  sudo ./setup_minio.sh
  ```
2. Установка зависимостей
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

Использование
Загрузка файла:
Отправьте POST-запрос на /upload/ с PDF-файлом.
Скачивание файла:
Отправьте GET-запрос на /download/{filename}, заменив {filename} на имя файла.
Получение списка файлов:
Отправьте GET-запрос на /files/, чтобы получить список всех файлов в корзине pdf_files.
