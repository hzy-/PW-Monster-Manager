#imports up in this
from pymongo import Connection

# connect to db
def connect():
	#connect to database
	connection = Connection()
	db = connection.monster_manager
	return db



# test
monsters = connect().monsters

name = 'evil warlock teacher'
description = 'this is a despicable fiend that commonly dwells in school libraries'
level = 4
hit_points = 325
skill_points = 48478
resistances = (
	{'attribute': 'physical', 'resistance': 'weak'},
	{'attribute': 'fire', 'resistance': 'resist'},
	{'attribute': 'ice', 'resistance': 'null'},
	{'attribute': 'lightning', 'resistance': 'absorb'},
	{'attribute': 'wind', 'resistance': 'reflect'},
	{'attribute': 'light', 'resistance': 'N/A'},
	{'attribute': 'dark', 'resistance': 'N/A'}
	)
skills = (
	{'skill': 'jump on walls'},
	{'skill': 'throw cars'},
	{'skill': 'take photos'},
	{'skill': 'do good at maths'}
	)
natural_attacks = (
	{'name': 'sharpie', 'cost': 234563, 'hits': 5467, 'damage': 53748, 'ailment': 'makes me head feel all fuzzy', 'critical': 12, 'notes': 'this is one deadly pen, not to be messed with'},
	{'name': 'bic', 'cost': 234563, 'hits': 5467, 'damage': 53748, 'ailment': 'makes me head feel all fuzzy', 'critical': 12, 'notes': 'this is one deadly pen, not to be messed with'},
	{'name': 'faber castell', 'cost': 234563, 'hits': 5467, 'damage': 53748, 'ailment': 'makes me head feel all fuzzy', 'critical': 12, 'notes': 'this is one deadly pen, not to be messed with'}
	)

monster = {
	'name': name,
	'level': level,
	'hit_points': hit_points,
	'skill_points': skill_points,
	'resistances': resistances,
	'skills': skills,
	'natural_attacks': natural_attacks,
	'description': description,
	'official': True
	}
#id = monsters.insert(monster)
#print id
