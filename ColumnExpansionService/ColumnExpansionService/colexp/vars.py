class Vars(object):
    """Variables for the Application"""

    APP_VERSION="1.0"

    #Variables
    CONN_STR = "DRIVER={{ODBC Driver 11 for SQL Server}}; SERVER={0}; DATABASE={1}; Trusted_Connection=yes;"
    LOG_FORMAT_STR = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DATE_FORMAT_STR = "%Y%m%d-%H%M%S"
    LOG_FILE="log\z-columnExpansion.log"
    INPUT_DATA=""

    def __new__(cls):
        return super(vars, cls).__new__()

    def __init__(self, *args, **kwargs):
        return super(vars, self).__init__(*args, **kwargs)

