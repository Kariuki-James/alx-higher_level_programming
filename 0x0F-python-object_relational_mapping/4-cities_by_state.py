#!/usr/bin/python3
'''
Lists all cities from a database
'''

from sys import argv
import MySQLdb


def list_cities(username, password, dbname):
    '''lists all cities.

    Args:
        username (str): mysql username
        password (str): mysql password
        dbname (str): mysql database name
    '''
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8"
            )
    cur = conn.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC;"
    cur.execute(sql)

    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    num_args = len(argv)
    if num_args < 4:
        print("3 arguments required: <username> <password> <dbname>")
    else:
        list_cities(argv[1], argv[2], argv[3])
