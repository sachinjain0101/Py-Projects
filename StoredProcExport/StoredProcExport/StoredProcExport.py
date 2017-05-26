import pyodbc

connStr = "DRIVER={{ODBC Driver 11 for SQL Server}}; SERVER={0}; DATABASE={1}; Trusted_Connection=yes;"
connStr = connStr.format("L-9560-0101","TimeHistory")

#Establishing database connection
conn = pyodbc.connect(connStr)

# Connect to the database
conn = pyodbc.connect(connStr)
cursor = conn.cursor()

##
# Export a stored procedure using its name and connected cursor
# @param string name: The name of the procedure to export
# @return string
##
def exportProcedure(name):
    try:
        sql = "EXEC sp_helptext N'" + name + "';"
        cursor.execute(sql)
        rows1 = cursor.fetchall()
        content = ""
        for r in rows1:
            content += r.Text.strip() + "\n"
        return content.encode('utf-8').strip()
    except:
        print name
        return ""

# Get a list of system objects sorted by views, tables, procedures, and
# functions created by the user
sql = """SELECT SPECIFIC_CATALOG+'.'+SPECIFIC_SCHEMA+'.'+SPECIFIC_NAME AS SP_NAME FROM INFORMATION_SCHEMA.routines 
         WHERE ROUTINE_SCHEMA NOT LIKE 'CIGNIFY%'
         ORDER BY 1"""
cursor.execute(sql)
rows = cursor.fetchall()

# Export each of the stored procedures and functions
content = ""
for r in rows:
    f = open(r.SP_NAME + ".sql", "w")
    content = exportProcedure(r.SP_NAME)
    f.write(content + "\n\n")
    f.close()

conn.close()
