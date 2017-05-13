from flask import Flask, render_template, request, jsonify, Response, Blueprint
''', session, g, redirect, url_for, abort, , flash'''

import json

job = Blueprint('job', __name__)

url_stem = '/job'

@job.route(url_stem, methods=['GET'])
def get():
	return []

@job.route(url_stem, methods=['POST'])
def post():
	if not request.json: abort(400)

	json_str = str(request.json)
	s = json.dumps(json_str, sort_keys=True, indent=2, separators=(',', ': '))
	print(s)

	dto = {"fish": "bird"}

	return Response(json.dumps(dto), mimetype='application/json')


	return 200

@job.route(url_stem, methods=['DELETE'])
def delete():
	if not request.json: abort(400)

	return 200