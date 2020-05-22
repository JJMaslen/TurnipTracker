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

def add_entry(conn, entry, sql):
    cur = conn.cursor()
    cur.execute(sql, entry)
    return cur.lastrowid

def update_entry(conn, entry, sql):
    cur = conn.cursor()
    cur.execute(sql, entry)
    conn.commit()

def read_table(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    return rows

def createTable_weekPrices():
    file = open("weekPricesPath.txt", "r")
    database = str(file.read())
    file.close()

    sql_create_weekPrices_table = """ CREATE TABLE IF NOT EXISTS weekPrices (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        mondayAM integer,
                                        mondayPM integer,
                                        tuesdayAM integer,
                                        tuesdayPM integer,
                                        wednesdayAM integer,
                                        wednesdayPM integer,
                                        thursdayAM integer,
                                        thursdayPM integer,
                                        fridayAM integer,
                                        fridayPM integer
                                    ); """
    
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_weekPrices_table)
    else:
        print("Error! Cannot create the database connection")

def createTable_turnipTable():
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql_create_turnipTable_table = """ CREATE TABLE IF NOT EXISTS turnipTable (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        price integer,
                                        date text,
                                        active text

                                    ); """
    
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_turnipTable_table)

    else:
        print("Error! Cannot create the database connection")

def editTable_turnipTable_addActive():
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql_update_turnipTable = """ ALTER TABLE turnipTable
              ADD active text"""
    
    conn = create_connection(database)

    c = conn.cursor()
    c.execute(sql_update_turnipTable)

def addEntry_turnipTable(id, userName, price, currentTime):
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql = ''' INSERT INTO turnipTable(id,name,price,date) 
              VALUES(?,?,?,?) '''
    conn = create_connection(database)
    with conn:
        NewEntry = (id, userName, price, currentTime)
        add_entry(conn, NewEntry, sql)

def addEntry_weekPrices(id, userName, price, dayTime):
    file = open("weekPricesPath.txt","r")
    database = str(file.read())
    file.close()

    sql = 0 #call method here
    conn = create_connection(database)
    with conn:
        NewEntry = (id, userName, price)
        add_entry(conn, NewEntry, sql)

def updateEntry_turnipTable(id, price, currentTime):
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql = ''' UPDATE turnipTable
              SET price = ? ,
                  date = ?
              WHERE id = ?'''
    conn = create_connection(database)
    with conn:
        update_entry(conn, (price, currentTime, id), sql)

def readTable_turnipTable():
    file = open("databasePath.txt", "r")
    database = str(file.read())
    file.close()

    sql = '''SELECT * FROM turnipTable
             ORDER BY 
                price DESC'''
    conn = create_connection(database)
    with conn:
        data = read_table(conn, sql)
    return data