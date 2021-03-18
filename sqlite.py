import sqlite3
conn = sqlite3.connect('PythonPassUtils.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS hasla
             (nazwa TEXT, haslo TEXT)''')
# ALl fine, TODO class for reading and adding
conn.commit()
conn.close()