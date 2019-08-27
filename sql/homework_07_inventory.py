"""
Count the total number of orders for each model

PRINT
model
quantity
order count
"""

def get_quantity():
    """gets the quantity of cars and prints it"""
    c.execute("""SELECT quantity FROM inventory 
            WHERE model=?""", (m[1],))
    quantity = c.fetchall()
    print('Quantity:', quantity[0][0])

def get_order_count():
    """gets the order count and prints it"""
    c.execute("SELECT count(order_date) FROM orders \
            WHERE model=?", (m[1],))
    count = c.fetchall()
    print('Order count:', count[0][0], '\n')

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT make, model FROM orders""")
    models = c.fetchall()

    all = c.execute("SELECT * FROM orders")

    rows = c.fetchall()
    
    for m in models:
        print('Model:', m[0], m[1])
        get_quantity()
        get_order_count()
