import sqlite3

conn = sqlite3.connect('pmanalysis.db')
c = conn.cursor()

#to view tables, download Browser for SQLite at https://github.com/sqlitebrowser/sqlitebrowser/releases
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS login(email VARCHAR(255), password1 VARCHAR(255), password2 VARCHAR(255), register DATETIME, verified BOOLEAN)')

def data_entry():
    c.execute('INSERT INTO login VALUES("example@email.com", "cse123", "cse123", "2018-01-20 01:25:00.000", 1)')
    conn.commit()
    c.close()
    conn.close()

#create_table()
data_entry()
