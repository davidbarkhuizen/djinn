import os
import logging
import json
import sqlite3
from flask import Flask, render_template

def load_config(config_file_path='config.json'):

	with open(config_file_path) as json_file:
		return json.load(json_file)

def configure_logging(log_file_path, log_to_console=True):

	logging.basicConfig(filename=log_file_path, level=logging.INFO)

	if log_to_console: 
		logging.getLogger().addHandler(logging.StreamHandler())

database_file_path = None
def connect():
	db = sqlite3.connect(database_file_path)
	db.row_factory = sqlite3.Row
	return db

db = None
def get_db():
	global db
	db = db if db is not None else connect()
	return db

app = Flask('djinn')

@app.teardown_appcontext
def close_db(error):
	get_db().close()

@app.route('/', methods=['GET'])
def show_entries():
	return render_template('index.html', error=None)

# --------------------------------------------------------------------------------

config = load_config()

root_path = os.path.expanduser(config['root_path'])
database_file_path = os.path.join(root_path, config['database_file_name'])

log_file_path = os.path.join(root_path, config['log_file_name'])
configure_logging(log_file_path)

from api.job import job
app.register_blueprint(job)

# host='0.0.0.0'
app.run(debug=config['debug'], port=config['server_port'])