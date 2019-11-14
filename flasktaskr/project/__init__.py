# project/__init__.py

from flask import flask
from flask_sqlalchemy import sqlalchemy

app = Flask(__name_)
app.config.from_pyfile('_config.py')
db =SQLAlchemy(app)

from project.users.views import users_blueprint
from project.tasks.views import tasks_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(tasks_blueprint)


