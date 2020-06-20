"""
sqlite
mysql
oracle
postgreSQL
"""

import sqlite3
DB = 'testDB.db'
TABLE = 'comments'


def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn.cursor()


def execute(query, db_name):
    response = connect_db(db_name).execute(query)
    return response


def show_data(resp):
    for row in resp.fetchall():
        print(row)


def close_conn(conn):
    conn.close()


try:
    cnx = connect_db(DB)
    data = execute("select * from {} where post_id=3;".format(TABLE), DB)
    show_data(data)
except sqlite3.OperationalError:
    print("Database not found")
