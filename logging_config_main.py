# logging_config.py
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.NOTSET,  # Capture all log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(levelname)s - %(message)s',  # Format of the log messages
        handlers=[
            logging.StreamHandler(),  # Output logs to console
            logging.FileHandler('app.log')  # Output logs to a file
        ]
    )
