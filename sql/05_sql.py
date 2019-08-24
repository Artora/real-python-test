
# INSERT Command with Error Handler


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 840000)"
)
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)"
)

    # commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print("Oops! The database does not exist. \
Please check the name and correct it.")

# close the database connection
conn.close()

# table population is misnamed as populations on purpose to
# get an error message
