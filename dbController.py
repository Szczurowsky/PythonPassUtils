import sqlite3
import mysqlData


class ObjectController:
    def __init__(self, db_type, name, password):
        self.db_type = db_type
        self.name = name
        self.password = password

    def update_objects(self, passwd, object_id):
        if self.db_type == int(2):
            cursor = mysqlData.db.cursor()
            cursor.execute("UPDATE `password` SET`password`= %s WHERE ID = %s", (passwd, object_id,))
            mysqlData.db.commit()
            return True
        if self.db_type == int(1):
            try:
                conn = sqlite3.connect('PythonPassUtils.sqlite')
            except Exception as e:
                return e
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS password
                         (id integer PRIMARY KEY, name TEXT, password TEXT)''')
            object_id = int(object_id)
            c.execute('''UPDATE `password` SET`password`= ? WHERE ID = ?;''', (passwd, object_id,))
            conn.commit()
            return True

    def remove_objects(self, object_id):
        if self.db_type == int(2):
            cursor = mysqlData.db.cursor()
            cursor.execute("DELETE FROM password WHERE ID = %s", (object_id,))
            mysqlData.db.commit()
            mysqlData.db.close()
            return True
        if self.db_type == int(1):
            try:
                conn = sqlite3.connect('PythonPassUtils.sqlite')
            except Exception as e:
                return e
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS password
                         (id integer PRIMARY KEY, name TEXT, password TEXT)''')
            object_id = int(object_id)
            c.execute('''DELETE FROM password WHERE ID = ?;''', (object_id,))
            conn.commit()
            return True

    def show_objects(self):
        if self.db_type == int(2):
            cursor = mysqlData.db.cursor()
            try:
                cursor.execute('SELECT * FROM password')
                rows = cursor.fetchall()
                print('========== Passwords ==========')
                print('ID Name Password')
                for row in rows:
                    print(row)
                print('========== Passwords ==========')
                mysqlData.db.commit()
                return True
            except Exception as e:
                return e

        if self.db_type == int(1):
            try:
                conn = sqlite3.connect('PythonPassUtils.sqlite')
            except Exception as e:
                return e
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS password
                         (id integer PRIMARY KEY, name TEXT, password TEXT)''')
            try:
                c.execute('''SELECT * FROM password''')
                rows = c.fetchall()
                print('========== Passwords ==========')
                print('ID Name Password')
                for row in rows:
                    print(row)
                print('========== Passwords ==========')
                return True
            except Exception as e:
                return e

    def add_object(self):
        if self.db_type == int(2):
            cursor = mysqlData.db.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS `pythonpassutils`.`password` ( `ID` INT(255) NOT NULL AUTO_INCREMENT , '
                '`username` '
                'VARCHAR(255) NOT NULL , `password` VARCHAR(255) NOT NULL , PRIMARY KEY (`ID`)) ENGINE = InnoDB;')
            cursor.execute("INSERT INTO `password`(`ID`, `username`, `password`) VALUES (%s, %s, %s)",
                           (None, self.name, self.password))
            mysqlData.db.commit()
            return True
        if self.db_type == int(1):
            try:
                conn = sqlite3.connect('PythonPassUtils.sqlite')
            except Exception as e:
                return e
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS password
                         (id integer PRIMARY KEY, name TEXT, password TEXT)''')
            c.execute('''INSERT INTO password VALUES(?, ?, ?)''', (None, self.name, self.password))
            conn.commit()
            return True
