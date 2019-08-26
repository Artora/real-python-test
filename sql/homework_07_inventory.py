"""
Count the total number of orders for each model


PRINT
model
quantity
order count

"""

def order_count(model_name):
    count = ("SELECT count(order_date) FROM orders \
        WHERE model=model_name")
    print(count)

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT count(order_date) FROM orders \
            WHERE model='Mustang'")
    print(c.fetchall())

    c.execute("""SELECT DISTINCT make, model FROM orders""")
    models = c.fetchall()

    all = c.execute("SELECT * FROM orders")

    rows = c.fetchall()
    print('test')
    print(models)
    print(type(models))
    for m in models:
        print(m[0], m[1])
        lel = m[1]
        print(type(lel))
        print(lel + 'yodli')
        mus = ('Mustang')
        c.execute("SELECT count(order_date) FROM orders WHERE model=?", (mus,))
        count = c.fetchall()
        print(count)
