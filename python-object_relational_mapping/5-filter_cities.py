#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa. The script is safe from SQL injection
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
    state_name = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities \
        LEFT JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))
    row_result = cursor.fetchall()
    cities = [row[0]
              for row in row_result]
    print(", ".join(cities))
    cursor.close()
    db.close()

