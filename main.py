from bottle import route, run, debug
from db import connect
from pystache import render
from bson.objectid import ObjectId

#generale stuff
base_pagename = 'Persona: Wildcard | Monster Manager'
db = connect()

def generate_template(template_name):
	header = open('templates/header.html').read()
	footer = open('templates/footer.html').read()
	template = open('templates/'+template_name+'.html').read()

	return header+template+footer

@route('/')
def home():
	monsters = db.monsters.find({'official': True})

	#pystache up in this
	t = generate_template('index')
	c = {'monsters': monsters, 'page_name': base_pagename}
	r = render(t, c)
	return r

@route('/monsters/:id/')
def single_monster(id):
	monster = db.monsters.find_one({'_id': ObjectId(id)})
	print id
	t = generate_template('single_monster')
	page_name = base_pagename+' / Monster / '+monster['name'] #['name']
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

debug(True)
run(host='localhost', port=8080, reloader=True)
