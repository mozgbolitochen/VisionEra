# Берем легкую версию Python
FROM python:3.9-slim

# Создаем папку приложения внутри контейнера
WORKDIR /app

# Копируем список библиотек и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем сам код
COPY . .

# Открываем порт, на котором работает Streamlit
EXPOSE 8501

# Команда для запуска сайта
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]