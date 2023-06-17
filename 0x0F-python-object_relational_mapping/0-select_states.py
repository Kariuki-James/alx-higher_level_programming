#!/usr/bin/python3
'''MySQLdb connection to insert states
'''

import MySQLdb
import sys

if __name__ != "__main__":
    sys.exit()

num_args = len(sys.argv)
if num_args < 4:
    print("3 arguments required: <username> <passwd> <dbname>")
    sys.exit()

conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
        )
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
result = cur.fetchall()
for row in result:
    print(row)
cur.close()
conn.close()
