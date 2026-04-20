import streamlit as st

# Настройка страницы
st.set_page_config(page_title="VisionEra Dashboard", layout="wide")

st.title("📹 VisionEra - Система наблюдения")
st.write("Добро пожаловать в панель управления камерами (MVP версия).")

# Боковая панель для навигации
st.sidebar.header("Управление")
camera_choice = st.sidebar.selectbox(
    "Выберите камеру для просмотра:",
    ["Камера 1 (Главный вход)", "Камера 2 (Коридор)", "Камера 3 (Серверная)"]
)

# Главный экран
st.subheader(f"Трансляция: {camera_choice}")

# Статус
st.success("Статус: Устройство в сети. Идет трансляция.")

# Имитация картинки с камеры (заглушки из интернета)
if camera_choice == "Камера 1 (Главный вход)":
    st.image("https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80", caption="Прямой эфир: Вход", use_column_width=True)
elif camera_choice == "Камера 2 (Коридор)":
    st.image("https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80", caption="Прямой эфир: Коридор", use_column_width=True)
else:
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80", caption="Прямой эфир: Серверная", use_column_width=True)

st.divider()

# Лог событий
st.write("Лог системы:")
st.code("""
[12:00:01] Система инициализирована
[12:02:15] Подключение к Камере 1 - Успешно
[12:05:30] Движение не зафиксировано
""", language="text")