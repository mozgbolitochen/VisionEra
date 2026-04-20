import streamlit as st
import psycopg2
import os
from datetime import datetime

st.set_page_config(page_title="VisionEra Professional", layout="wide")

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
camera = st.sidebar.selectbox("Камера:", ["Вход", "Склад"])
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