
"Cube object representing a 3x3 Rubix cube."

import random

class Cube(object):
	def __init__(self):
		self.faces = [
			["R", "R", "R", "R", "R", "R", "R", "R", "R"],
			["O", "O", "O", "O", "O", "O", "O", "O", "O"],
			["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
			["G", "G", "G", "G", "G", "G", "G", "G", "G"],
			["B", "B", "B", "B", "B", "B", "B", "B", "B"],
			["V", "V", "V", "V", "V", "V", "V", "V", "V"]
		]

		# index faces of cube
		self.front = 0
		self.right = 1
		self.back = 2
		self.left = 3
		self.top = 4
		self.bottom = 5

	def randomize(self, twists):
		while twists > 0:
			twist_choice= random.randint(0, 3)
			index = random.randint(0,2)
			if twist_choice is 0:
				twist_row_right(index)
			elif twist_choice is 1:
				twist_row_left(index)
			elif twist_choice is 2:
				twist_col_up(index)
			elif twist_choice is 3:
				twist_col_down(index)
			twists -= 1

	def twist_row_right(self, row):
		self.twist_right(row)
		if row is 0:
			self.twist_face_right(self.top)
		elif row is 2: 
			self.twist_face_right(self.bottom)

	def twist_row_left(self, row):
		self.twist_left(row)
		if row is 0:
			self.twist_face_left(self.top)
		elif row is 2:
			self.twist_face_left(self.bottom)

	def twist_col_up(self, col):
		self.twist_up(col)
		if col is 0:
			self.twist_face_left(self.left)
		elif col is 2:
			self.twist_face_left(self.right)

	def twist_col_down(self, col):
		self.twist_down(col)
		if col is 0:
			self.twist_face_right(self.left)
		elif col is 2:
			self.twist_face_right(self.right)

	def twist_top_row_right(self, row):
		self.twist_top_right(row)
		if row is 0:
			self.twist_face_right(self.back)
		elif row is 2:
			self.twist_face_right(self.front)

	def twist_top_row_left(self, row):
		self.twist_top_left(row)
		if row is 0:
			self.twist_face_left(self.back)
		elif row is 2:
			self.twist_face_right(self.front)

	def twist_right(self, row):
		temp = self.copy_face(self.faces[self.front])
		self.replace_row(self.faces[self.left], self.faces[self.front], row)
		self.replace_row(self.faces[self.back], self.faces[self.left], row)
		self.replace_row(self.faces[self.right], self.faces[self.back], row)
		self.replace_row(temp, self.faces[self.right], row)

	def twist_left(self, row):
		temp = self.copy_face(self.faces[self.front])
		self.replace_row(self.faces[self.right], self.faces[self.front], row)
		self.replace_row(self.faces[self.back], self.faces[self.right], row)
		self.replace_row(self.faces[self.left], self.faces[self.back], row)
		self.replace_row(temp, self.faces[self.left], row)

	def replace_row(self, replacing_face, face_to_replace, row):
		index = row * 3
		face_to_replace[index] = replacing_face[index]
		face_to_replace[index + 1] = replacing_face[index + 1]
		face_to_replace[index + 2] = replacing_face[index + 2]

	def twist_up(self, col):
		temp = self.copy_face(self.faces[self.front])
		self.replace_col(self.faces[self.bottom], self.faces[self.front], col)
		self.replace_col(self.faces[self.back], self.faces[self.bottom], col)
		self.replace_col(self.faces[self.top], self.faces[self.back], col)
		self.replace_col(temp, self.faces[self.top], col)

	def twist_down(self, col):
		temp = self.copy_face(self.faces[self.front])
		self.replace_col(self.faces[self.top], self.faces[self.front], col)
		self.replace_col(self.faces[self.back], self.faces[self.top], col)
		self.replace_col(self.faces[self.bottom], self.faces[self.back], col)
		self.replace_col(temp, self.faces[self.bottom], col)

	def replace_col(self, replacing_face, face_to_replace, col):
		face_to_replace[col] = replacing_face[col]
		face_to_replace[col + 3] = replacing_face[col + 3]
		face_to_replace[col + 6] = replacing_face[col + 6]

	def twist_top_right(self, row):
		temp = self.copy_face(self.faces[self.top])
		self.col_to_row_right(self.faces[self.left], self.faces[self.top], row)
		self.row_to_col_right(self.faces[self.bottom], self.faces[self.left], row)
		self.col_to_row_right(self.faces[self.right], self.faces[self.bottom], row)
		self.row_to_col_right(temp, self.faces[self.right], row)

	def col_to_row_right(self, col_face, row_face, row):
		row_index = row * 3
		col_index = row
		row_face[row_index] = col_face[col_index + 6]
		row_face[row_index + 1] = col_face[col_index + 3]
		row_face[row_index + 2] = col_face[col_index]

	def row_to_col_right(self, row_face, col_face, row):
		row_index = row * 3
		col_index = row
		col_face[col_index] = row_face[row_index]
		col_face[col_index + 3] = row_face[row_index + 1]
		col_face[col_index + 6] = row_face[row_index + 2]

	def twist_top_left(self, row):
		temp = self.copy_face(self.faces[self.top])
		self.col_to_row_left(self.faces[self.right], self.faces[self.top], row)
		self.row_to_col_left(self.faces[self.bottom], self.faces[self.right], row)
		self.col_to_row_left(self.faces[self.left], self.faces[self.bottom], row)
		self.row_to_col_left(temp, self.faces[self.left], row)

	def col_to_row_left(self, col_face, row_face, row):
		row_index = row * 3
		col_index = row
		row_face[row_index] = col_face[col_index]
		row_face[row_index + 1] = col_face[col_index + 3]
		row_face[row_index + 2] = col_face[col_index + 6]

	def row_to_col_left(self, row_face, col_face, row):
		row_index = row * 3
		col_index = row
		col_face[col_index] = row_face[row_index + 2]
		col_face[col_index + 3] = row_face[row_index + 1]
		col_face[col_index + 6] = row_face[row_index]

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

	def load_faces(self, faces):
		count = 0
		while count < 6:
			row_index = 0
			while row_index < 9:
				self.faces[count][row_index] = faces[count][row_index]
				row_index += 1
			count += 1

	def reset(self):
		self.faces = [
			["R", "R", "R", "R", "R", "R", "R", "R", "R"],
			["O", "O", "O", "O", "O", "O", "O", "O", "O"],
			["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
			["G", "G", "G", "G", "G", "G", "G", "G", "G"],
			["B", "B", "B", "B", "B", "B", "B", "B", "B"],
			["V", "V", "V", "V", "V", "V", "V", "V", "V"]
		]
