# MinIO File Storage

![Minio Console](minio.jpg) 


## Особенности
- Установка и запуск MiniO: setup_minio.sh
- Создание тестовых файлов: create_files.py
- Получение списка корзин и файлов: list_buckets.py

## Установка
- Установка и запуск Minio в Linux(Ubuntu)
```bash
  git clone https://github.com/froyzan/Minio.git
  cd Minio
  chmod +x setup_minio.sh
  sudo ./setup_minio.sh
```
- Установка и запуск Minio в Kubernetes
```bash
  cd k8s
  kubectl apply -f minio.yml
```

## Работа с корзинами 
- Установка зависимостей
```bash
  pip install -r requirements.txt
```
- Создание и загрузка файлов
```bash
  python3 create_files.py
```
- Вывод списка корзин и файлов
```bash
  python3 list_buckets.py
```
![List buckets](list_buckets.jpg) 

`<link>` : <http://localhost:9001>
```html
  User: minioadmin
  Password: minioadmin
```
