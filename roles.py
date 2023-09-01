roles = {
	'3D Printing': 'Phoenix',
	'Fusion360': 'Phoenix',
	'Solid Works': 'Phoenix',
	'Large Format Printing': 'Phoenix',
	'CAD': 'Fred',
	'Adobe Suite': 'Aza',
	'Python': 'Fred',
	'C++': 'Fred',
	'Javascript': 'Fred',
	'Microcontrollers (Arduino/Teensy)': 'Phoenix, Fred',
	'Circuit Design': 'Phoenix, Fred',
	'RPis': 'Phoenix',
	'Sensors': 'Phoenix',
	'Motors': 'Phoenix',
	'Soldering': 'Fred',
	'Mechanical Design': 'Phoenix',
	'Human Centered Design': 'Bella',
	'Screenprinting': 'Bella',
	'Circut vinyl cutting': 'Bella',
	'Jewelry making': 'Aza',
	'Painting and Drawing': 'Aza',
	'Sewing': 'Bella',
	'Fiber Arts': 'Bella',
	'Paper craft': 'Aza',
	'Pin making': 'Bella',
	'Power tools': 'Aza',
	'Plant care': 'Bella',
	'Zero Waste Management': 'Bella'
}

# print(roles.get('Zero Waste Management'))

request = input("What do you need help with? \n")

def lookup_role(r):
	if r in roles.keys():
		print(roles.get(r))
	else:
		print('Sorry, we can\'help with that.')

lookup_role(request)
