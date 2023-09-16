#!/usr/bin/python3
"""
    Model to list all cities of a state given as argument
    from the database hbtn_0e_0_usa.
    safe from MySQL injections.
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
    sql = "SELECT cities.name from cities\
            JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %s\
            ORDER BY cities.id"
    cursor.execute(sql, (argv[4],))
    print(', '.join([city_name[0] for city_name in cursor.fetchall()]))
    cursor.close()
    connection.close()
