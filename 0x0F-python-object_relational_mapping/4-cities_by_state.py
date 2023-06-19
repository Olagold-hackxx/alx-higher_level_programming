#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa where
name matches the argument"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    db_conn = MySQLdb.connect(host='localhost',
            port=3306,
            user=db_user,
            passwd=db_passwd,
            db=db_name)
    cur = db_conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN (states) ON cities.state_id = states.id ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
