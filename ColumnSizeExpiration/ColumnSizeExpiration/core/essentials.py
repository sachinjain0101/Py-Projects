import os
import logging

class Vars(object):
    '''Variables for the Application'''
    APP_VERSION='1.0'
    #Variables
    CONN_STR = 'DRIVER={{ODBC Driver 11 for SQL Server}}; SERVER={0}; DATABASE={1}; Trusted_Connection=yes;'
    LOG_FORMAT_STR = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DATE_FORMAT_STR = '%Y%m%d-%H%M%S'
    LOG_DIR='log'
    LOG_FILE='z-columnExpansion.log'
    OUT_DIR='out'
    INPUT_DATA=''

    EMAIL_FROM='sachin.jain@peoplenet.com'
    EMAIL_TO='sachinjain.0101@gmail.com'
    SMTP_ADDR='smtp.office365.com:587'
    SMTP_USER='sachin.jain@peoplenet.com'
    SMTP_PWD=''
    MESSAGE = '\r\n'.join(['From: {0}',
              'To: {1}',
              'MIME-Version: 1.0',
              'Content-type: text/html',
              'Subject: Column Expiration Report: {2}',
              '',
              '{3}'])

    HTML_TMPL_STR="""
                  <!DOCTYPE html>
                  <html>
                  <body>
                  <table border="1" cellpadding="5" cellspacing="5">
                  <col width="300">
                  <col width="300">
                  <th>Table Name</th>
                  <th>Days to Expire</th>
                  {0}
                  </table>  
                  </body>
                  </html>
                  """

    def __new__(cls):
        return super(vars, cls).__new__()

    def __init__(self, *args, **kwargs):
        return super(vars, self).__init__(*args, **kwargs)

def getAppLogger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logdir = os.path.join(os.getcwd(),Vars.LOG_DIR)
        if not os.path.isdir(logdir):
            #shutil.rmtree(logdir)
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

