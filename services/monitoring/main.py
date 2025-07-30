#!/usr/bin/env python3
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Monitoring service started")
    
    while True:
        try:
            logger.info("Monitoring is running...")
            # Здесь будет логика мониторинга
            time.sleep(30)
        except KeyboardInterrupt:
            logger.info("Monitoring stopped")
            break
        except Exception as e:
            logger.error(f"Error in monitoring: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
