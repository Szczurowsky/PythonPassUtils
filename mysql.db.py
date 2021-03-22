import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
cursor = db.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS PythonPassUtils')
cursor.execute('USE PythonPassUtils')
# Works TODO Get and insert
db.close()
