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

def create_entry(conn, entry):

    sql = ''' INSERT INTO turnipTable(id,name,price,date) 
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, entry)
    return cur.lastrowid

def update_entry(conn, entry):
    sql = ''' UPDATE turnipTable
              SET price = ?'''

def createTable():
    pass
def addEntry():
    pass
def updateEntry():
    pass

def setUp():
    database = r"F:\Projects\Repositories\TurnipTracker\db\turnip.db"

    sql_create_turnipTable_table = """ CREATE TABLE IF NOT EXISTS turnipTable (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        price integer,
                                        date text

                                    ); """
    
    conn = create_connection(database)
    with conn:
        thing = (1234567890, "Jordan", 600, "29/03 09:26")
        create_entry(conn, thing)

    if conn is not None:
        create_table(conn, sql_create_turnipTable_table)

    else:
        print("Error! Cannot create the database connection")