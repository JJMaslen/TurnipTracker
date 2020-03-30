import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_entry(conn, entry):

    sql = ''' INSERT INTO turnipTable(id,name,price,date) 
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, entry)
    return cur.lastrowid

def update_entry(conn, entry):
    sql = ''' UPDATE turnipTable
              SET price = ? ,
                  date = ?
              WHERE id = ?'''

    cur = conn.cursor()
    cur.execute(sql, entry)
    conn.commit()

def read_table(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM turnipTable")

    rows = cur.fetchall()
    return rows

def createTable():
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql_create_turnipTable_table = """ CREATE TABLE IF NOT EXISTS turnipTable (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        price integer,
                                        date text

                                    ); """
    
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_turnipTable_table)

    else:
        print("Error! Cannot create the database connection")

def addEntry(id, userName, price, currentTime):
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    conn = create_connection(database)
    with conn:
        NewEntry = (id, userName, price, currentTime)
        add_entry(conn, NewEntry)

def updateEntry(id, price, currentTime):
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    conn = create_connection(database)
    with conn:
        update_entry(conn, (price, currentTime, id))

def readTable():
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    conn = create_connection(database)
    with conn:
        data = read_table(conn)
    return data