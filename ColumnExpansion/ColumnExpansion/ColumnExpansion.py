from CustomLogging import CustomLogging
import os
import pyodbc
import sys

#Initializing logger 
logger = CustomLogging();
logger.log("Starting: "+__name__)
logger.log(logger.version)

#Variables
connStr = "DRIVER={{ODBC Driver 11 for SQL Server}}; SERVER={0}; DATABASE={1}; Trusted_Connection=yes;"

#Building database connection
server = "L-9560-0101"
db = "TimeHistory"

args=sys.argv
if len(args)>1:
    server = sys.argv[1]
    db = sys.argv[2]

connStr=connStr.format(server,db)
logger.log("Connection String = "+connStr)

#Establishing database connection
conn = pyodbc.connect(connStr)

#Open sql file
fileName = "drop_create_constraints_indexes.sql"
fileName = os.path.join(os.getcwd(),fileName)
logger.log(fileName)

fh = open(fileName,"r")

for line in fh.readlines():
    print line

fh.close()


cursor = conn.cursor() 
cursor.execute('SELECT current_timestamp')  
row = cursor.fetchone()  
while row:
    print str(row[0])  
    row = cursor.fetchone()  


