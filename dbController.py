import sqlite3
import mysql.connector


class ObjectController:
    def __init__(self, db_type, name, password):
        self.db_type = db_type
        self.name = name
        self.password = password

    def show_objects(self):
        if self.db_type == int(2):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = db.cursor()
            cursor.execute('CREATE DATABASE IF NOT EXISTS PythonPassUtils')
            cursor.execute('USE PythonPassUtils')
            db.close()
        if self.db_type == int(1):
            try:
                conn = sqlite3.connect('PythonPassUtils.sqlite')
            except Exception as e:
                return e
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS password
                         (name TEXT, password TEXT)''')
            try:
                c.execute('''SELECT * FROM password''')
                rows = c.fetchall()
                for row in rows:
                    print(row)
                conn.close()
                return True
            except Exception as e:
                return e

    def add_object(self):
        if self.db_type == int(2):
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = db.cursor()
            cursor.execute('CREATE DATABASE IF NOT EXISTS PythonPassUtils')
            cursor.execute('USE PythonPassUtils')
            db.close()
        if self.db_type == int(1):
            try:
                conn = sqlite3.connect('PythonPassUtils.sqlite')
            except Exception as e:
                return e
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS password
                         (name TEXT, password TEXT)''')
            c.execute('''INSERT INTO password VALUES(?, ?)''', (self.name, self.password))
            conn.commit()
            conn.close()
            return True
