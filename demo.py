import sys

from src.ANPR.logger import logging
from src.ANPR.exception import CustomException

def test():
    try:
        logging.info("Testing our logging module")
        x = 1/0
    except Exception as e:
        raise CustomException(e,sys)
        print(e)
    
if __name__=="__main__":
    try:
        test()
    except Exception as e:
        print("in except")
        print(e)