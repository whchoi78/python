import mysql.connector
 
db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="p@ssw0rd", 
    database="mydb", 
    auth_plugin="mysql_native_password"
)

print(db_conn)

db_cursor = db_conn.cursor()
