#!/usr/bin/python3
"""Lists all states with name starting with N"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=db_user,
                         passwd=db_passwd,
                         db=db_name)
    cur = db.cursor()
    cur.execute('SELECT id, name FROM states\
                WHERE name REGEXP "^N" ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
