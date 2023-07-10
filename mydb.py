import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='ouss99',
)
cursor = dataBase.cursor()
cursor.execute('CREATE DATABASE crm')
print("Database created successfully")
