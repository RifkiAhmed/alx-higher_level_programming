#!/usr/bin/python3
"""
    Model to list all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
    )
    cursor = connection.cursor()
    sql = "SELECT * from states ORDER BY id"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
