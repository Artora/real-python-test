



"""
Create new table orders
fields:
make, model, order_date

3 records for each car

Ford Mustang 2
Ford Escort 20
Ford Focus 45
Honda Civic 25
Honda Accord 40


"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    orders = [
    ('Ford', 'Mustang', '2019-08-25'),
    ('Ford', 'Mustang', '2019-01-01'),
    ('Ford', 'Mustang', '2018-04-04'),

    ('Ford', 'Escort', '2019-07-17'),
    ('Ford', 'Escort', '2019-05-23'),
    ('Ford', 'Escort', '2019-05-02'),

    ('Ford', 'Focus', '2019-08-22'),
    ('Ford', 'Focus', '2019-08-04'),
    ('Ford', 'Focus', '2019-07-15'),

    ('Honda', 'Civic', '2019-06-25'),
    ('Honda', 'Civic', '2019-06-14'),
    ('Honda', 'Civic', '2019-06-03'),

    ('Honda', 'Accord', '2019-05-29'),
    ('Honda', 'Accord', '2019-03-09'),
    ('Honda', 'Accord', '2019-01-16')
    ]

    c.execute("CREATE TABLE orders(Make TEXT, Model TEXT, order_date DATE)")
    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)
