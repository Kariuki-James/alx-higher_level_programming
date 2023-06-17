#!/usr/bin/python3
'''1-filter_states module
Lists states with filtered names
'''

from sys import argv
import MySQLdb


def search_state(username, password, dbname, state_name):
    '''searches for a state in states table

    Args:
        username (str): mysql username
        password (str): mysql password
        dbname (str): mysql database name
        state_name (str): state to search for
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
    sql = "SELECT * FROM states \
            WHERE states.name = %s \
            ORDER BY states.id ASC;"
    cur.execute(sql, (state_name,))

    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    num_args = len(argv)
    if num_args < 5:
        print("4 arguments required: <username> <password> "
              "<dbname> <state_name>")
    else:
        search_state(argv[1], argv[2], argv[3], argv[4])
