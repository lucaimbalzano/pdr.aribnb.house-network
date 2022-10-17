# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


import datetime 
import logging

logger = logging.getLogger()
currentDate = datetime.date.today()
time_now = currentDate.strftime("%Y-%m-%d")

path = ".\\console\\log\\"
hdlr = logging.FileHandler(path + time_now+'-logger-pdr.log')
formatter = logging.Formatter('PDR.AIRBNB.HOUSE-NETWORK:  %(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def get_logger():
    return logger