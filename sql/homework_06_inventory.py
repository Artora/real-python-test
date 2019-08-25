
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()


    c.execute("""SELECT DISTINCT inventory.make, inventory.model, 
        inventory.quantity, orders.order_date
        FROM inventory, orders 
        WHERE inventory.model = orders.model""")

    rows = c.fetchall()
    b = False
    for r in rows:
        a = r[2]
        if a != b:
            print('\n' + r[0], r[1])
            print('Quantity ' +str(r[2]))
            print("Order dates: ")
        print(r[3])
        b = r[2]
