#!/usr/bin/python3
"""
    Model to list all states with name matches user input
    from the database hbtn_0e_0_usa.
    safe from MySQL injection.
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
    sql = "SELECT * from states\
            WHERE name LIKE BINARY %s ORDER BY id"
    cursor.execute(sql, (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
