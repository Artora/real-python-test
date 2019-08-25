
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    