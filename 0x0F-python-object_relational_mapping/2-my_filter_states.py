#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa where
name matches the argument"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    nameMatch = argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=db_user,
                         passwd=db_passwd,
                         db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states\
                WHERE name = '{}' ORDER BY id ASC""".format(nameMatch))
    rows = cur.fetchall()
    for row in rows:
        print(row)
