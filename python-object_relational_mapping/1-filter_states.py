#!/usr/bin/python3

"""
Script that lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%'ORDER BY id ASC")
    row_result = cursor.fetchall()
    for row in row_result:
        print(row)
    cursor.close()
    db.close()

