
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
			["R", "R", "R", "R", "R", "R", "R", "R", "R"],
			["O", "O", "O", "O", "O", "O", "O", "O", "O"],
			["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
			["G", "G", "G", "G", "G", "G", "G", "G", "G"],
			["B", "B", "B", "B", "B", "B", "B", "B", "B"],
			["P", "P", "P", "P", "P", "P", "P", "P", "P"]
		]

	def twist_row_right(self, row):
		self.twist_right(row)
		if row is 0:
			self.twist_face_right(TOP)
		elif row is 2: 
			self.twist_face_right(BOTTOM)

	def twist_right(self, row):
		temp = ["", "", "", "", "", "", "", "", ""]
		temp_index = 0
		for item in self.faces[FRONT]:
			temp[temp_index] = self.faces[FRONT][temp_index]
			temp_index += 1

		self.replace_row(self.faces[LEFT], self.faces[FRONT], row)
		self.replace_row(self.faces[BACK], self.faces[LEFT], row)
		self.replace_row(self.faces[RIGHT], self.faces[BACK], row)
		self.replace_row(temp, self.faces[RIGHT], row)

	def twist_face_right(self, face):
		grid = self.faces[face]
		temp = grid[0]
		grid[0] = grid[6]
		grid[6] = grid[8]
		grid[8] = grid[2]
		grid[2] = temp

		temp = grid[1]
		grid[1] = grid[3]
		grid[3] = grid[7]
		grid[7] = grid[5]
		grid[5] = temp

	def replace_row(self, replacing_face, face_to_replace, row):
		index = row * 3
		face_to_replace[index] = replacing_face[index]
		face_to_replace[index + 1] = replacing_face[index + 1]
		face_to_replace[index + 2] = replacing_face[index + 2]

	def print_faces(self):
		for y in self.faces:
			print ''.join(y)


if __name__ == '__main__':
	print "Testing Cube object."
	cube = Cube()
	cube.twist_row_right(0)
	cube.print_faces()