#!/usr/bin/python3

"""
 This script connects to a MySQL database, retrieves all states sorted
 by ID in ascending order,
 and prints the results to the console
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    row_result = cursor.fetchall()
    for row in row_result:
        print(row)
    cursor.close()
    db.close()

