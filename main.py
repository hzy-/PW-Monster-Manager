from bottle import route, run, debug
from db import connect
from pystache import render

#generale stuff
base_pagename = 'Persona: Wildcard | Monster Manager'
db = connect().monsters

def generate_template(template_name):
	header = open('templates/header.html').read()
	footer = open('templates/footer.html').read()
	template = open('templates/'+template_name+'.html').read()

	return header+template+footer

@route('/')
def home():
	monsters = db.find({'official': True})

	#pystache up in this
	t = generate_template('index')
	c = {'monsters': monsters, 'page_name': base_pagename}
	r = render(t, c)
	return r

@route('/monsters/:id/')
def single_monster(id):
	monster = db.find_one({'_id': id})

	t = generate_template('single_monster')
	page_name = base_pagename+' / Monster / '+monster['_id'] #['name']
	c = {'monster': monster, 'page_name': page_name}
	r = render(t, c)
	return r

debug(True)
run(host='localhost', port=8080, reloader=True)
