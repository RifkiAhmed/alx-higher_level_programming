#!/usr/bin/python3
"""
    Model to list all states with name starting with 'N'
    from the database hbtn_0e_0_usa
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
    sql = "SELECT * from states WHERE name = '{}' ORDER BY id".format(argv[4])
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
