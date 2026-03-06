#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
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

    # The %s is the placeholder for the variable, providing security
    query = """SELECT cities.id, cities.name, states.name
                FROM cities JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;"""

    cursor.execute(query)

    # Fetching all the rows returned by the query
    rows = cursor.fetchall()

    # Displaying the results in the required format
    for row in rows:
        print(row)

    # Closing the cursor and the database connection
    cursor.close()
    db.close()
