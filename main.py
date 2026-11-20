import logging
from datetime import datetime

# Налаштування logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

# Отримання поточної дати
today = datetime.now().strftime("%Y-%m-%d")

# Запис повідомлення рівня INFO
logging.info(f"Поточна дата: {today}")
