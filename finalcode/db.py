import pymysql

def get_db_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1928374650@asD",
        database="willazilla",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn