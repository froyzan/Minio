#!/bin/bash

check_program() {
    if ! command -v "$1" &> /dev/null; then
        echo "$1 не установлена. Устанавливаю..."
        sudo apt update
        sudo apt install -y "$1"
    else
        echo "$1 уже установлена."
    fi
}

check_minio() {
    if ! command -v "$1" &> /dev/null; then
        echo "$1 не установлена. Устанавливаю..."
        wget https://dl.min.io/server/minio/release/linux-amd64/minio -O minio
        chmod +x minio
        sudo mv minio /usr/local/bin/
    else
        echo "$1 уже установлена."
    fi
}

check_program "wget"
check_minio "minio"

# Создание директории для хранения данных
DATA_DIR="/mnt/data"
sudo mkdir -p $DATA_DIR
sudo chown $USER:$USER $DATA_DIR
export MINIO_ROOT_USER="minioadm"
export MINIO_ROOT_PASSWORD="miniopass"

# Запуск MinIO в фоновом режиме
if pidof "minio" > /dev/null; then
    echo "Minio уже запущен."
else
    echo "Minio не запущен. Запускаю..."
    # Запуск скрипта в фоновом режиме
    nohup minio server --console-address ":9001" $DATA_DIR --address ":9000" --quiet &
fi

# Вывод информации о доступе к MinIO
echo "URL: http://localhost:9000"
echo "Консоль: http://localhost:9001"
echo "Логин: $MINIO_ROOT_USER"
echo "Пароль: $MINIO_ROOT_PASSWORD"
