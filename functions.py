# Commonly used functions

def generate_template(template_name):
	header = open('templates/header.html').read()
	footer = open('templates/footer.html').read()
	template = open('templates/' + template_name + '.html').read()

	return header + template + footer