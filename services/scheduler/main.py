#!/usr/bin/env python3
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Scheduler service started")
    
    while True:
        try:
            logger.info("Scheduler is running...")
            # Здесь будет логика планировщика
            time.sleep(60)
        except KeyboardInterrupt:
            logger.info("Scheduler stopped")
            break
        except Exception as e:
            logger.error(f"Error in scheduler: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
