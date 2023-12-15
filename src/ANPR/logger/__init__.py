import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.txt"

LOG_DIR = "logs"

os.makedirs(LOG_DIR,exist_ok=True) #if Directory Exist, then it does not create Directory

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
 filemode="w",
 filename=LOG_FILE_PATH,
 level=logging.INFO,
 format="[%(asctime)s]%(lineno)d%(name)s - %(levelname)s %(message)s")

