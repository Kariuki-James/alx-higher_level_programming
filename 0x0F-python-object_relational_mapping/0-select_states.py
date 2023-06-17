#!/usr/bin/python3
'''0-select_states module
Lists all states from hbtn_0e_0_usa.states
'''

from sys import argv
import MySQLdb


def list_all_states(username, password, dbname):
    '''lists all states from hbtn_0e_0_usa.states

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
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

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
        list_all_states(argv[1], argv[2], argv[3])
