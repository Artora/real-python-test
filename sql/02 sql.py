

import sqlite3

conn = sqlite3.connect("cars.db")

curosr = conn.cursor()

cursor.execute("""CREATE TABLE inventory
                (Make TEXT, Model TEXT, Quantity INT)
                """)

conn.close()

