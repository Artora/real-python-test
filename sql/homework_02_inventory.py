
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
    ('Ford', 'Mustang', 1),
    ('Ford', 'Escort', 20),
    ('Ford', 'Focus', 45),
    ('Honda', 'Civic', 15),
    ('Honda', 'Accord', 40)
    ]

    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)


