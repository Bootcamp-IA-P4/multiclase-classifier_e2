# Используем Python 3.9 как базовый образ
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libgomp1 \
 && rm -rf /var/lib/apt/lists/*


# Обновляем pip перед установкой зависимостей
RUN pip install --upgrade pip

# Копируем файлы зависимостей
COPY requirements-docker.txt .

# Устанавливаем зависимости с явным указанием версий
RUN pip install --no-cache-dir -r requirements-docker.txt

# Копируем код приложения
COPY . .

# Открываем порты
EXPOSE 8000 8050

# Запускаем оба сервера (FastAPI и Dash)
CMD ["sh", "-c", "uvicorn app.api:app --host 0.0.0.0 --port 8000 & python app/front.py"]