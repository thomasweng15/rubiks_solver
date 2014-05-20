
"Cube object representing a 3x3 Rubix cube."

# index faces of cube
FRONT = 0
RIGHT = 1
BACK = 2
LEFT = 3
TOP = 4
BOTTOM = 5

class Cube(object):
	def __init__(self):
		self.faces = [
			[["R", "R", "R"],["R", "R", "R"],["R", "R", "R"]],
			[["O", "O", "O"],["O", "O", "O"],["O", "O", "O"]],
			[["Y", "Y", "Y"],["Y", "Y", "Y"],["Y", "Y", "Y"]],
			[["G", "G", "G"],["G", "G", "G"],["G", "G", "G"]],
			[["B", "B", "B"],["B", "B", "B"],["B", "B", "B"]],
			[["P", "P", "P"],["P", "P", "P"],["P", "P", "P"]]
		]

	def twist_right(self, row):
		if row is 0:
			print "adjust top faces"
		elif row is 2: 
			print "adjust bottom faces"
		else:
			print "only swap intermediary colors?"

	def print_faces(self):
		print "front"
		for y in self.faces:
			for x in y:
				print ''.join(x)
			print ""


if __name__ == '__main__':
	print "Testing Cube object."
	cube = Cube()
	#cube.print_faces()
	cube.twist_right()