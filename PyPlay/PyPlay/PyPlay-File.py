import logging
import os
import shutil

class Vars(object):
    """Variables for the Application"""
    APP_VERSION="1.0"
    #Variables
    CONN_STR = "DRIVER={{ODBC Driver 11 for SQL Server}}; SERVER={0}; DATABASE={1}; Trusted_Connection=yes;"
    LOG_FORMAT_STR = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DATE_FORMAT_STR = "%Y%m%d-%H%M%S"
    LOG_DIR="log"
    LOG_FILE="z-columnExpansion.log"
    OUT_DIR="out"
    INPUT_DATA=""
    def __new__(cls):
        return super(vars, cls).__new__()

    def __init__(self, *args, **kwargs):
        return super(vars, self).__init__(*args, **kwargs)

def getAppLogger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logdir = os.path.join(os.getcwd(),Vars.LOG_DIR)
        if os.path.isdir(logdir):
            shutil.rmtree(logdir)
        os.mkdir(logdir,0777)
        logfile = os.path.join(logdir,Vars.LOG_FILE)
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


logger = getAppLogger(__name__)
logger.info('START')

outdir=os.path.join(os.getcwd(),Vars.OUT_DIR)
if os.path.isdir(outdir):
    shutil.rmtree(outdir)

os.mkdir(outdir,0777)

count=0
while count<20:
    fl=os.path.join(outdir,str(count)+".txt")
    f=open(fl,'a')
    i=0
    while i<= count:
        f.write(str(count)*i*100+'\n')
        i+=1
    f.close()
    count+=1

logger.info('END')
