
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

	def twist_row_left(self, row):
		self.twist_left(row)
		if row is 0:
			self.twist_face_left(TOP)
		elif row is 2:
			self.twist_face_left(BOTTOM)

	def twist_col_up(self, col):
		self.twist_up(col)
		if col is 0:
			self.twist_face_left(LEFT)
		elif col is 2:
			self.twist_face_left(RIGHT)

	def twist_col_down(self, col):
		self.twist_down(col)
		if col is 0:
			self.twist_face_right(LEFT)
		elif col is 2:
			self.twist_face_right(RIGHT)

	def twist_right(self, row):
		temp = copy_face(self.faces[FRONT])
		self.replace_row(self.faces[LEFT], self.faces[FRONT], row)
		self.replace_row(self.faces[BACK], self.faces[LEFT], row)
		self.replace_row(self.faces[RIGHT], self.faces[BACK], row)
		self.replace_row(temp, self.faces[RIGHT], row)

	def twist_left(self, row):
		temp = copy_face(self.faces[FRONT])
		self.replace_row(self.faces[RIGHT], self.faces[FRONT], row)
		self.replace_row(self.faces[BACK], self.faces[RIGHT], row)
		self.replace_row(self.faces[LEFT], self.faces[BACK], row)
		self.replace_row(temp, self.faces[LEFT], row)

	def replace_row(self, replacing_face, face_to_replace, row):
		index = row * 3
		face_to_replace[index] = replacing_face[index]
		face_to_replace[index + 1] = replacing_face[index + 1]
		face_to_replace[index + 2] = replacing_face[index + 2]

	def twist_up(self, col):
		temp = self.copy_face(self.faces[FRONT])
		self.replace_col(self.faces[BOTTOM], self.faces[FRONT], col)
		self.replace_col(self.faces[BACK], self.faces[BOTTOM], col)
		self.replace_col(self.faces[TOP], self.faces[BACK], col)
		self.replace_col(temp, self.faces[TOP], col)

	def twist_down(self, col):
		temp = self.copy_face(self.faces[FRONT])
		self.replace_col(self.faces[TOP], self.faces[FRONT], col)
		self.replace_col(self.faces[BACK], self.faces[TOP], col)
		self.replace_col(self.faces[BOTTOM], self.faces[BACK], col)
		self.replace_col(temp, self.faces[BOTTOM], col)

	def replace_col(self, replacing_face, face_to_replace, col):
		face_to_replace[col] = replacing_face[col]
		face_to_replace[col + 3] = replacing_face[col + 3]
		face_to_replace[col + 6] = replacing_face[col + 6]

	def copy_face(self, face):
		temp = ["", "", "", "", "", "", "", "", ""]
		temp_index = 0
		for item in face:
			temp[temp_index] = face[temp_index]
			temp_index += 1
		return temp

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

	def twist_face_left(self, face):
		grid = self.faces[face]
		temp = grid[0]
		grid[0] = grid[2]
		grid[2] = grid[8]
		grid[8] = grid[6]
		grid[6] = temp

		temp = grid[1]
		grid[1] = grid[5]
		grid[5] = grid[7]
		grid[7] = grid[3]
		grid[3] = temp

	def print_faces(self):
		count = 0
		row = ""
		for y in self.faces:
			for x in y:
				row += x
				count += 1
				if count is 3:
					print row 
					row = ""
					count = 0
			print ""


if __name__ == '__main__':
	print "Testing Cube object."
	cube = Cube()
	cube.twist_col_up(0)
	cube.print_faces()