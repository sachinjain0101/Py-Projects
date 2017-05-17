from CustomLogging import CustomLogging
import os
import pyodbc

 
if __name__ == "__main__":
    logger = CustomLogging();
    logger.log("Hey")


logger.log(os.getcwd())


fileName = os.path.join(os.getcwd(),'sj.txt')
logger.log(fileName)
fh = open(fileName,"w")
fh.write("hello hello")
fh.close()

print pyodbc.drivers()


conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 11 for SQL Server}; SERVER=L-9560-0101; DATABASE=TimeHistory; Trusted_Connection=yes;'
    )

cursor = conn.cursor() 
cursor.execute('SELECT current_timestamp')  



row = cursor.fetchone()  



while row:
    print str(row[0])  
    row = cursor.fetchone()  

print '{} {}'.format('one', 'two')