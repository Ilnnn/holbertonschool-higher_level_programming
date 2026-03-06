#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists 
all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the MySQL server and executes a JOIN query to 
    filter cities by a specific state name provided as an argument.
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

    # The 4th argument is the name of the state to filter by
    state_name = sys.argv[4]

    # SQL query using JOIN and a placeholder for security against injections
    query = """SELECT cities.name
                FROM cities 
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""

    cursor.execute(query, (state_name,))

    # Fetching all the rows returned by the query
    rows = cursor.fetchall()

    # Displaying results as a comma-separated list on a single line
    print(", ".join([row[0] for row in rows]))

    # Closing the cursor and the database connection
    cursor.close()
    db.close()
