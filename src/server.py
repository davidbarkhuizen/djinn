import os
import logging

import sys
import sqlite3
from flask import Flask, render_template, request, jsonify, Response
import json
''', session, g, redirect, url_for, abort, , flash'''

user_home_path = os.path.expanduser("~")

INFO_LOG_FILE_NAME = os.path.join(user_home_path, 'data', 'djinn.server.info.log')
logging.basicConfig(filename=INFO_LOG_FILE_NAME, level=logging.INFO)

DEBUG_LOG_FILE_NAME = os.path.join(user_home_path, 'data', 'djinn.server.debug.log')
logging.basicConfig(filename=DEBUG_LOG_FILE_NAME, level=logging.DEBUG)

logging.getLogger().addHandler(logging.StreamHandler())

logging.info('info')
logging.debug('debug')

# --------------------------------------------------------------------------------
# DATA ACCESS LAYER

DATABASE_FILE_PATH = os.path.join(user_home_path, 'data', 'djinn.sql3.db')

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

app = Flask('djinn')


@app.teardown_appcontext
def close_db(error):
    get_db().close()


@app.route('/', methods=['GET'])
def show_entries():
    log('GOT')
    return render_template('index.html', error=None)


# --------------------------------------------------------------------------------

@app.route('/job', methods=['POST'])
def create_job():

    log('DAWG')

    if not request.json:
        abort(400)

    '''
    json_str = str(request.json)
    json.dumps(json_str, sort_keys=True, indent=2, separators=(',', ': '))
    '''

    dto = {"fish": "bird"}

    return Response(json.dumps(dto), mimetype='application/json')


# --------------------------------------------------------------------------------

app.run(debug=True)