# logging is important for tracking events when the application runs.which help in debugging and monitoring the application behaviour.

import logging
import os   # it provide a funcationality (or handle all files) for reading and writing to the file system.
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
print(LOG_FILE)
logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE)
print(logs_path)
# os.getcwd() -> it give the current directory you are in right now.
# os.path.join -> joining all the three directory i.e, os.getcwd(),logs,LOG_FILE

# Creating directory
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)s - %(levelname)s - %(message)s',
    level=logging.INFO
)