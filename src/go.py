import os
import sqlite3
from flask import Flask, render_template
'''request, session, g, redirect, url_for, abort, , flash'''

user_home_path = os.path.expanduser("~")

# --------------------------------------------------------------------------------

DATABASE_FILE_PATH = os.path.join(user_home_path, 'data', 'drunkenmaster.sql3.db')

def connect():
	db = sqlite3.connect(DATABASE_FILE_PATH)
	db.row_factory = sqlite3.Row
	return db

db = None
def get_db():
	global db
	db = db if db is not None else connect()
	return db

# --------------------------------------------------------------------------------

app = Flask('drunken master')

@app.teardown_appcontext
def close_db(error):
	get_db().close()

@app.route('/')
def show_entries():
	return render_template('index.html', error=None)

# --------------------------------------------------------------------------------


 if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

# --------------------------------------------------------------------------------

app.run()