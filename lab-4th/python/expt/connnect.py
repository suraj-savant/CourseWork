
# Importing module
import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "insurance"
)

cursor = mydb.cursor()
cursor.execute("show tables;")
for db in cursor :
    print(db)
 
# Printing the connection object
print(mydb)