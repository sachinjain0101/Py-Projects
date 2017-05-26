import logging
import os
from colexp import Vars

# setting up logger
def getAppLogger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logfile = os.path.join(os.getcwd(),Vars.LOG_FILE)
        logging.basicConfig(level=logging.NOTSET
                            , filename=logfile
                            , format=Vars.LOG_FORMAT_STR
                            , datefmt=Vars.DATE_FORMAT_STR
                            , filemode='a')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter(Vars.LOG_FORMAT_STR, datefmt=Vars.DATE_FORMAT_STR)
        console.setFormatter(formatter)
        logger.addHandler(console)
    
    return logger
