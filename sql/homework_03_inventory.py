
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET quantity=2 WHERE Model='Mustang'")
    c.execute("UPDATE inventory SET quantity=25 WHERE Model='Civic'")

    c.execute("SELECT * FROM inventory")

    data = c.fetchall()

    for row in data:
        print(row[0], row[1], row[2])

