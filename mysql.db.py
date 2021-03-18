import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
cursor = mydb.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS PythonPassUtils')
cursor.execute('USE PythonPassUtils')
