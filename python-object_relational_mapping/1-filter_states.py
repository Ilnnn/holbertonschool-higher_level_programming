#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the MySQL server and retrieves states
    starting with the letter N.
    """
    # Database connection using arguments from the command line
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # Executing the query with specific columns and BINARY for case sensitivity
    cursor.execute("""SELECT id, name
                FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY id ASC;""")

    # Fetching all the rows returned by the query
    rows = cursor.fetchall()

    # Displaying the results in the required format
    for row in rows:
        print(row)

    # Closing the cursor and the database connection
    cursor.close()
    db.close()
