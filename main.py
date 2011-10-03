from bottle import route, run, debug
from db import connect
import pystache

@route('/')
def home():
	db = connect().monsters
	monsters = db.find({'official': True})

	#pystache up in this
	t = open('templates/index.html').read()
	c = {'monsters': monsters, 'page_name': 'Persona: Wildcard | Monster Manager'}
	t_out = pystache.render(t, c)
	return t_out



debug(True)
run(host='localhost', port=8080, reloader=True)
