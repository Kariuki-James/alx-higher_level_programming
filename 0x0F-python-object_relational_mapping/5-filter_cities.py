#!/usr/bin/python3
'''
Lists all cities of a given state
'''

from sys import argv
import MySQLdb


def list_state_cities(username, password, dbname, state_name):
    '''lists all cities of a given state

    Args:
        username (str): mysql username
        password (str): mysql password
        dbname (str): mysql database name
        state_name (str): name of the state to list cities
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
    sql = "SELECT cities.name \
            FROM cities INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE BINARY states.name = %s \
            ORDER BY cities.id ASC;"
    cur.execute(sql, (state_name,))

    result = cur.fetchall()
    print(", ".join([row[0] for row in result]))
    cur.close()
    conn.close()


if __name__ == "__main__":
    num_args = len(argv)
    if num_args < 5:
        print("3 arguments required: <username> <password>"
              "<dbname> <state_name>")
    else:
        list_state_cities(argv[1], argv[2], argv[3], argv[4])
