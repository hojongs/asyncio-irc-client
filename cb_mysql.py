import pymysql as mysql # python3.5 mysql connector

HOST = 'localhost'
USER = 'root'
PASS = 'pass'
DB = 'test_db'
TB = 'chat_tb'

conn = None
cur = None
query = 'INSERT INTO %s VALUE(%s, %s)'

def init_mysql(): # callback
    print('init_mysql')
    global conn, cur
    conn = mysql.connect(host=HOST, user=USER,password=PASS,db=DB,charset='utf8mb4',cursorclass=mysql.cursors.DictCursor)
    cur = conn.cursor()

def log_to_mysql(nick, chat): # callback
    print('log_to_mysql')
    global conn, cur
    cur.execute(query % (TB, nick, chat))
    conn.commit()

def close_mysql(): # callback
    print('close_mysql')
    global conn, cur
    cur.close()
    conn.close()
    