import os
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    # Здесь можно добавить другие настройки или функциональность, если необходимо
    logger.info("Переменная окружения установлена: %s", os.environ['DJANGO_SETTINGS_MODULE'])
except Exception as e:
    logger.error("Ошибка при установке переменной окружения: %s", e)