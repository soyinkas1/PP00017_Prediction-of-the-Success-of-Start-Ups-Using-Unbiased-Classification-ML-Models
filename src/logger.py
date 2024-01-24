import logging
import os
import sys
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
<<<<<<< HEAD
        logging.FileHandler(logs_path),
=======
        logging.FileHandler(LOG_FILE_PATH),
>>>>>>> 9689df6e094e9fbb9f579de2889952f36c70d7df
        logging.StreamHandler(sys.stdout)
    ]

)
