from openpyxl import Workbook
from vars import Vars
import openpyxl
import threading
import os
import pyodbc
import sys
import time
import logging

# setting up logger

logFile = os.path.join(os.getcwd(),Vars.logFile)
logging.basicConfig(level=logging.NOTSET
                    , filename=logFile
                    , format=Vars.formatStr
                    , datefmt=Vars.dateFmtStr
                    , filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(Vars.formatStr, datefmt=Vars.dateFmtStr)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def seperator():
    logging.info("*" * 60)
    
# simple log test
seperator()
logging.info("starting... " + __name__ + " " + Vars.version)
seperator()

def myfunc(i):
    logging.info("sleeping 5 sec from thread %d" % i)
    time.sleep(5)
    logging.info("finished sleeping from thread %d" % i)

for i in range(10):
    t = threading.Thread(target=myfunc, args=(i,))
    t.start()


wb = Workbook()
wb = openpyxl.load_workbook(filename="input-data.xlsx")
ws = wb["data"]
for row in ws.rows:
    for cell in row:
        logging.info(cell.value)

#Building database connection
server = "L-9560-0101"
db = "TimeHistory"

args = sys.argv
if len(args) > 1:
    server = sys.argv[1]
    db = sys.argv[2]

connStr = Vars.connStr.format(server,db)
logging.info("Connection String = " + connStr)

#Establishing database connection
conn = pyodbc.connect(connStr)

#Open sql file
fileName = "drop_create_constraints_indexes.sql"
fileName = os.path.join(os.getcwd(),fileName)
logging.info(fileName)

print(os.listdir(os.getcwd()))

#fh = open(fileName,"r")

#for line in fh.readlines():
#    print line
#fh.close()


cursor = conn.cursor() 
cursor.execute('SELECT current_timestamp')  
row = cursor.fetchone()  
while row:
    print str(row[0])  
    row = cursor.fetchone()  


sys.exit(0)