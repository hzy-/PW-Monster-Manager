#! /usr/bin/python

from bottle import route, run, request, get, post, put, delete, debug, redirect, static_file
from db import connect
from pystache import render
from bson.objectid import ObjectId
from functions import *

#generale stuff
base_pagename = 'Persona: Wildcard | Monster Manager'
db = connect()

#on to the routing
@route('/static/:path#.+#')
def serve_static(path):
	return static_file(path, root='static')


@get('/')
def home():
	monsters = db.monsters.find({'official': True})
	#pystache up in this
	t = generate_template('index')
	c = {'monsters': monsters, 'page_name': base_pagename}
	r = render(t, c)
	return r

@get('/monsters/new/')
def new_monster_form():
	t = generate_template('new_monster')
	c = {'page_name': base_pagename + ' / New Monster'}
	r = render(t, c)
	return r

@get('/monsters/:id/')
def view_monster(id):
	monster = db.monsters.find_one({'_id': ObjectId(id)})
	if monster['name'] is not None:
		t = generate_template('single_monster')
		page_name = base_pagename + ' / Monster / ' + monster['name']
		c = {
			#all that monster magic
			'name': monster['name'],
			'level': monster['level'],
			'hit_points': monster['hit_points'],
			'skill_points': monster['skill_points'],
			'resistances': monster['resistances'],
			'skills': monster['skills'],
			'natural_attacks': monster['natural_attacks'],
			'description': monster['description'],
			#and the other stuff
			'page_name': page_name
			}
		r = render(t, c)
		return r
	else:
		return 'monster not found :c'

@delete('/monsters/:id/')
def delete_monster(id):
	monster = db.monsters.find_one({'_id': ObjectId(id)})
	if monster['name'] is not None:
		db.monsters.remove(monster['_id'])
		return 'success!'

@post('/monsters/')
def create_monster():
	return Monster_from_json(request.POST['json'])



	

@get('/login/')
def login_form():
	t = generate_template('login')
	c = {'page_name': base_pagename+' / Login'}
	r = render(t, c)
	return r

debug(True)
run(host='localhost', port=8082, reloader=True)