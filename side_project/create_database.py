import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='*******'
)

mycursor = mydb.cursor()

# create a new database in MySQL
mycursor.execute('CREATE DATABASE superstore')

# close the connection
mydb.close()