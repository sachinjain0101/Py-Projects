from openpyxl import workbook
import threading
import os
import pyodbc
import sys
import time
import logging
import vars

# setting up logger
formatStr = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
dateFmtStr = "%Y%m%d-%H%M%S"

logFile = os.path.join(os.getcwd(),"log\z-columnExpansion.log")
logging.basicConfig(level=logging.NOTSET
                    , filename=logFile
                    , format=formatStr
                    , datefmt=dateFmtStr
                    , filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(formatStr, datefmt=dateFmtStr)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def seperator():
    logging.info("*" * 60)
    
# simple log test
seperator()
logging.info("starting... " + __name__ + " " + vars.vars.version)
seperator()

def myfunc(i):
    logging.info("sleeping 5 sec from thread %d" % i)
    time.sleep(5)
    logging.info("finished sleeping from thread %d" % i)

for i in range(10):
    t = threading.Thread(target=myfunc, args=(i,))
    t.start()

#Variables
connStr = "DRIVER={{ODBC Driver 11 for SQL Server}}; SERVER={0}; DATABASE={1}; Trusted_Connection=yes;"

wb = workbook()




#Building database connection
server = "L-9560-0101"
db = "TimeHistory"

args = sys.argv
if len(args) > 1:
    server = sys.argv[1]
    db = sys.argv[2]

connStr = connStr.format(server,db)
logging.info("Connection String = " + connStr)

#Establishing database connection
conn = pyodbc.connect(connStr)

#Open sql file
fileName = "drop_create_constraints_indexes.sql"
fileName = os.path.join(os.getcwd(),fileName)
logging.info(fileName)

print(os.listdir(os.getcwd()))

fh = open(fileName,"r")

#for line in fh.readlines():
#    print line
fh.close()


cursor = conn.cursor() 
cursor.execute('SELECT current_timestamp')  
row = cursor.fetchone()  
while row:
    print str(row[0])  
    row = cursor.fetchone()  


sys.exit(0)