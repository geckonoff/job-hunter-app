#!/usr/bin/env python3
import time
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Service started")
    
    # Бесконечный цикл для демона
    while True:
        try:
            # Здесь будет основная логика сервиса
            logger.info("Service is running...")
            time.sleep(60)  # Ждем 60 секунд
        except KeyboardInterrupt:
            logger.info("Service stopped by user")
            break
        except Exception as e:
            logger.error(f"Error in service: {e}")
            time.sleep(10)  # Подождать перед повтором

if __name__ == "__main__":
    main()
