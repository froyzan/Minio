#!/bin/bash

# Установка необходимых пакетов
sudo apt install -y wget

# Скачивание и установка MinIO
wget https://dl.min.io/server/minio/release/linux-amd64/minio -O minio
chmod +x minio
sudo mv minio /usr/local/bin/

# Создание директории для хранения данных
DATA_DIR="/mnt/data"
sudo mkdir -p $DATA_DIR
sudo chown $USER:$USER $DATA_DIR

MINIO_ROOT_USER="minioadmin"
MINIO_ROOT_PASSWORD="minioadmin"

# Запуск MinIO в фоновом режиме
nohup minio server --console-address ":9001" $DATA_DIR --address ":9000" --quiet &

# Вывод информации о доступе к MinIO
echo "MinIO запущен. Доступ к серверу:"
echo "URL: http://localhost:9000"
echo "Консоль: http://localhost:9001"
echo "Логин: $MINIO_ROOT_USER"
echo "Пароль: $MINIO_ROOT_PASSWORD"
