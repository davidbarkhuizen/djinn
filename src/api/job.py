from flask import Flask, render_template, request, jsonify, Response, Blueprint
''', session, g, redirect, url_for, abort, , flash'''

import json

job = Blueprint('job', __name__)

URL_STEM = '/job'

@job.route(URL_STEM, methods=['GET'])
def get():

	id = request.args.get('id')
	print('id {0}'.format(id))

	dto = {'id': id}
	return Response(json.dumps(dto), mimetype='application/json')

@job.route(URL_STEM, methods=['POST'])
def post():
	if not request.json: abort(400)

	reversed = {}

	for key in request.json.keys():
		val = request.json[key]
		
		reversed[key] = val[::-1] if type(val) == str	else val

	#s = json.dumps(json_str, sort_keys=True, indent=2, separators=(',', ': '))

	dto = reversed	
	return Response(json.dumps(dto), mimetype='application/json')
	# return 200

@job.route(URL_STEM, methods=['DELETE'])
def delete():
	if not request.json: abort(400)

	id = request.args.get('id')
	print('id {0}'.format(id))


	return 200 # with entity describing status
	# 202 = accepted => delete not yet enacted
	# 204 = no content => enacted, but response does not include an entity


