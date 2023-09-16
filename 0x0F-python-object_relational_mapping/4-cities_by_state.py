#!/usr/bin/python3
"""
    Model to list all cities from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = connection.cursor()
    sql = "SELECT cities.id, cities.name, states.name from cities\
            JOIN states\
            WHERE cities.state_id = states.id\
            ORDER BY cities.id"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
