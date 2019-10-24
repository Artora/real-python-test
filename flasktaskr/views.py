# project/views.py


#import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, \
    request, session, url_for, g

from forms import AddTaskForm, RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import datetime

from sqlalchemy.exc import IntegrityError

# config

app = Flask(__name__)
app.config.from_object('_config')
db = SQLAlchemy(app)

from models import Task, User

# helper functions
"""
def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])
"""

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# route handlers

@app.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Goodbye!')
    return redirect(url_for('login'))



@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    """
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
                or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash('Welcome!')
            return redirect(url_for('tasks'))
    return render_template('login.html')
    """

    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(\
                name = request.form['name']).first()
            if user is not None and \
                    user.password == request.form['password']:
                session['logged_in'] = True
                session['user_id'] = user.id
                flash('Welcome')
                return redirect(url_for('tasks'))
            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form = form, error = error)






@app.route('/tasks/')
@login_required
def tasks():
    """
    g.db = connect_db()
    cursor = g.db.execute(
        'select name, due_date, priority, task_id from tasks where status=1'
    )
    open_tasks = [
        dict(name=row[0], due_date=row[1], priority=row[2],
            task_id=row[3]) for row in cursor.fetchall()
    ]
    cursor = g.db.execute(
        'select name, due_date, priority, task_id from tasks where status=0'
    )
    closed_tasks = [
        dict(name=row[0], due_date=row[1], priority=row[2],
            task_id=row[3]) for row in cursor.fetchall()
    ]
    g.db.close()
    return render_template(
        'tasks.html',
        form = AddTaskForm(request.form),
        open_tasks = open_tasks,
        closed_tasks = closed_tasks
    )
    """
    """
    open_tasks = db.session.query(Task) \
        .filter_by(status = '1').order_by(Task.due_date.asc())
    closed_tasks = db.session.query(Task) \
        .filter_by(status = '0').order_by(Task.due_date.asc())
    return render_template(
        'tasks.html',
        form = AddTaskForm(request.form),
        open_tasks = open_tasks,
        closed_tasks = closed_tasks
    )
    """

    return render_template(
        'tasks.html',
        form = AddTaskForm(request.form),
        open_tasks = open_tasks(),
        closed_tasks = closed_tasks()
    )


# Add new tasks
@app.route('/add/', methods=['POST'])
@login_required
def new_task():
    """
    g.db = connect_db()
    name = request.form['name']
    date = request.form['due_date']
    priority = request.form['priority']
    if not name or not date or not priority:
        flash("All fields are required. Please try again.")
        return redirect(url_for('tasks'))
    else:
        g.db.execute('insert into tasks (\
            name, due_date, priority, status) \
            values (?, ?, ?, 1)', [
                request.form['name'],
                request.form['due_date'],
                request.form['priority']
            ]
        )
        g.db.commit()
        g.db.close()
        flash('New entry was successfully posted. Thanks')
        return redirect(url_for('tasks'))
    """

    error = None
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Task(
                form.name.data,
                form.due_date.data,
                form.priority.data,
                datetime.datetime.utcnow(),
                '1',
                session['user_id']
            )
            db.session.add(new_task)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            return redirect(url_for('tasks'))
        return render_template(
            'tasks.html',
            form = form,
            error = error,
            open_tasks = open_tasks(),
            closed_tasks = closed_tasks()
        )

    """
        else:
            return render_template('tasks.html', \
                form=form, error=error)
    return render_template('tasks.html, form=form, error=error')
    """

# Mark tasks as complete
@app.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
    """
    g.db = connect_db()
    g.db.execute(
        'update tasks set status = 0 where task_id='+str(task_id)
    )
    g.db.commit()
    g.db.close()
    flash('The task was marked as complete.')
    return redirect(url_for('tasks'))
    """

    new_id = task_id
    db.session.query(Task).filter_by(task_id = new_id).update({\
        "status": "0"})
    db.session.commit()
    flash('The task is complete. Nice.')
    return redirect(url_for('tasks'))



# Delete tasks
@app.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
    """
    g.db = connect_db()
    g.db.execute('delete from tasks where task_id='+str(task_id))
    g.db.commit()
    g.db.close()
    flash('The task was deleted.')
    return redirect(url_for('tasks'))
    """

    new_id = task_id
    db.session.query(Task).filter_by(task_id = new_id).delete()
    db.session.commit()
    flash('The task was deleted. Why not add a new one?')
    return redirect(url_for('tasks'))


@app.route('/register/', methods = ['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                form.name.data,
                form.email.data,
                form.password.data
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering. Please login.')
                return redirect(url_for('login'))
            except IntegrityError:
                error = 'That username and/or email already exist.'
                return render_template('register.html', \
                    form=form, error=error)
    return render_template('register.html', form = form, \
        error = error)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" %(
                getattr(form, field).label.text, error), 'error')

def open_tasks():
    return db.session.query(Task).filter_by(
        status='1').order_by(Task.due_date.asc())

def closed_tasks():
    return db.session.query(Task).filter_by(
        status='0').order_by(Task.due_date.asc())

