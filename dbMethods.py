import sqlite3
from datetime import datetime
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
                                        fridayPM integer,
                                        saturdayAM integer,
                                        saturdayPM integer
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

def addEntry_weekPrices(id, userName):
    file = open("weekPricesPath.txt","r")
    database = str(file.read())
    file.close()

    sql = ''' INSERT INTO weekPrices(id, name)
              VALUES(?,?) '''
    conn = create_connection(database)
    with conn:
        NewEntry = (id, userName)
        add_entry(conn, NewEntry, sql)

def updateEntry_weekPrices(id, price):
    file = open("weekPricesPath.txt","r")
    database = str(file.read())
    file.close()

    sql = dayDeterminer()
    conn = create_connection(database)
    with conn:
        NewEntry = (price, id)
        update_entry(conn, NewEntry, sql)

def dayDeterminer():
    currentWeekDay = datetime.now().weekday()
    currentTime = int(datetime.now().strftime('%H'))
    sql = ''' '''

    if currentWeekDay == 0 and currentTime < 12:
        sql = ''' UPDATE weekPrices
                  SET mondayAM = ? ,
                  WHERE id = ?'''
        print("Monday Morning")
    
    if currentWeekDay == 0 and currentTime >= 12:
        sql = ''' UPDATE weekPrices
                  SET mondayPM = ?
                  WHERE id = ?'''
        print("Monday Afternoon")
    
    if currentWeekDay == 1 and currentTime < 12:
        sql = ''' UPDATE weekPrices
                  SET tuesdayAM = ? ,
                  WHERE id = ?'''
        print("Tuesday Morning")
    
    if currentWeekDay == 1 and currentTime >= 12:
        sql = ''' UPDATE weekPrices
                  SET tuesdayPM = ? ,
                  WHERE id = ?'''
        print("Tuesday Afternoon")

    if currentWeekDay == 2 and currentTime < 12:
        sql = ''' UPDATE weekPrices
                  SET wednesdayAM = ? ,
                  WHERE id = ?'''
        print("Wednesday Morning")
    
    if currentWeekDay == 2 and currentTime >= 12:
        sql = ''' UPDATE weekPrices
                  SET wednesdayPM = ? ,
                  WHERE id = ?'''
        print("Wednesday Afternoon")

    if currentWeekDay == 3 and currentTime < 12:
        sql = ''' UPDATE weekPrices
                  SET thursdayAM = ? ,
                  WHERE id = ?'''
        print("Thursday Morning")
    
    if currentWeekDay == 3 and currentTime >= 12:
        sql = ''' UPDATE weekPrices
                  SET thursdayPM = ? ,
                  WHERE id = ?'''
        print("Thursday Afternoon")
    
    if currentWeekDay == 4 and currentTime < 12:
        sql = ''' UPDATE weekPrices
                  SET fridayAM = ? ,
                  WHERE id = ?'''
        print("Friday Morning")
    
    if currentWeekDay == 4 and currentTime >= 12:
        sql = ''' UPDATE weekPrices
                  SET fridayPM = ? ,
                  WHERE id = ?'''
        print("Friday Afternoon")

    if currentWeekDay == 5 and currentTime < 12:
        sql = ''' UPDATE weekPrices
                  SET saturdayAM = ? ,
                  WHERE id = ?'''
        print("Saturday Morning")
    
    if currentWeekDay == 5 and currentTime >= 12:
        sql = ''' UPDATE weekPrices
                  SET saturdayPM = ? ,
                  WHERE id = ?'''
        print("Saturday Afternoon")

    return sql

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

def readTable_weekPrices():
    file = open("weekPricesPath.txt","r")
    database = str(file.read())
    file.close()

    sql = '''SELECT * FROM weekPrices'''
    conn = create_connection(database)
    with conn:
        data = read_table(conn, sql)
    return data