import json

# Commonly used functions

def generate_template(template_name):
	header = open('templates/header.html').read()
	footer = open('templates/footer.html').read()
	template = open('templates/' + template_name + '.html').read()

	return header + template + footer

def Monster_from_json(input):
	monster = json.loads(input)
	# resistances
	try:
		resistances = monster['resistances']
	except:
		resistances = {}

	# skills
	try:
		skills = monster['skills']
	except:
		skills = []

	monster['skills'] = []
	for skill in skills:
		skill = {'skill': skill}
		monster['skills'].append(skill)

	# natural attacks
	try:
		natural_attacks = monster['natural_attacks']
	except:
		natural_attacks = []