class Vars(object):
    """Variables for the Application"""

    version="1.0"

    #Variables
    connStr = "DRIVER={{ODBC Driver 11 for SQL Server}}; SERVER={0}; DATABASE={1}; Trusted_Connection=yes;"
    formatStr = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    dateFmtStr = "%Y%m%d-%H%M%S"
    logFile="log\z-columnExpansion.log"
    inputData=""

    def __new__(cls):
        return super(vars, cls).__new__()

    def __init__(self, *args, **kwargs):
        return super(vars, self).__init__(*args, **kwargs)

