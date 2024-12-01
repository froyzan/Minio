# FastAPI MinIO File Storage

![Image Description](path/to/your/image.png) <!-- Замените на путь к вашему изображению -->

Это приложение на FastAPI позволяет загружать и скачивать PDF-файлы в локальное хранилище MinIO. 

## Особенности

- Загрузка PDF-файлов в корзину `pdf_files`.
- Скачивание PDF-файлов из корзины.
- Получение списка файлов в корзине с информацией о каждом файле.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   '''

2. Создайте виртуальное окружение (рекомендуется):
'''bash
python -m venv venv
source venv/bin/activate

3. Установите зависимостей:
pip install -r requirements.txt

Использование
Загрузка файла:
Отправьте POST-запрос на /upload/ с PDF-файлом.
Скачивание файла:
Отправьте GET-запрос на /download/{filename}, заменив {filename} на имя файла.
Получение списка файлов:
Отправьте GET-запрос на /files/, чтобы получить список всех файлов в корзине pdf_files.
