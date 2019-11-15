
# db_create.py

"""
import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()
"""
    # create the table
    #c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#        name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, 
    #    status INTEGER NOT NULL)""")
"""
    # insert dummy data into the table
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Finish this tutorial", "25.03.2015", 10, 1)'
    )
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Finish Real Python Course 2", "25.03.2015", 10, 1)'
    )
"""

# from views import db
# from models import Task
from datetime import date

from project import db
from project.models import Task, User

# create the database and the db table
db.create_all()

# insert data

db.session.add(
    User("admin", "ad@min.com", "admin", "admin")
)

db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, date(2015, 2, 13), 1, 1))
db.session.add(Task("Finish Real Python", date(2016, 10, 30), 10, date(2015, 2, 13), 1, 1))

# commit the changes
db.session.commit()


