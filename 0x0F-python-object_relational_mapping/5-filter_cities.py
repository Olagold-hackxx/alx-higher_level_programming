#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

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
    cur.execute("SELECT cities.name FROM cities\
                JOIN (states) ON cities.state_id = states.id\
                WHERE states.name = %s", (nameMatch,))
    rows = cur.fetchall()
    row_list = []
    for row in rows:
        row_list.append(row[0])
    print(', '.join(row_list))
