import streamlit as st
import psycopg2
import os
from datetime import datetime

st.set_page_config(page_title="VisionEra Professional", layout="wide") # Должно быть вызвано первым, НЕ МЕНЯТЬ

MEDIA_PATH = "./media"

st.sidebar.header("Наблюдение")
camera = st.sidebar.selectbox("Камера:", ["Вход", "Склад"])

st.subheader(f"Трансляция: {camera}")

photo_filename = "entrance.png" if camera == "Вход" else "warehouse.png"
photo_path = os.path.join(MEDIA_PATH, photo_filename)

if os.path.exists(photo_path):
    st.image(photo_path, caption=f"Прямой эфир — {camera}", use_column_width=True)
else:
    st.warning(f"Файл {photo_filename} не найден в папке media. Загрузите его на сервер.")
    st.image("https://i.ytimg.com/vi/0qslwZxdH4o/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGQgZChkMA8=&amp;rs=AOn4CLAHY9reFMDaJK4a0iTCHhK0QCSDuQ", use_column_width=True)

DB_NAME = os.getenv("POSTGRES_DB", "visionera_db")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "db")

def init_db():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS logs (id SERIAL PRIMARY KEY, event TEXT, time TIMESTAMP);")
    conn.commit()
    return conn, cur

st.title("📹 VisionEra Professional - Monitoring")

try:
    conn, cur = init_db()
    st.sidebar.success("Подключено к PostgreSQL")
except Exception as e:
    st.sidebar.error(f"Ошибка БД: {e}")

# Интерфейс
if st.button("Зафиксировать событие"):
    cur.execute("INSERT INTO logs (event, time) VALUES (%s, %s)", (f"Движение на {camera}", datetime.now()))
    conn.commit()
    st.toast("Событие сохранено в БД!")

# Вывод логов из БД
st.subheader("Последние события из базы данных:")
cur.execute("SELECT event, time FROM logs ORDER BY time DESC LIMIT 5")
rows = cur.fetchall()
for row in rows:
    st.write(f"🕒 {row[1].strftime('%H:%M:%S')} — {row[0]}")