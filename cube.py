
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
		moves = []
		while twists > 0:
			twist_choice = random.randint(0, 5)
			index = random.randint(0,2)
			if twist_choice is 0:
				self.twist_right(index)
			elif twist_choice is 1:
				self.twist_left(index)
			elif twist_choice is 2:
				self.twist_up(index)
			elif twist_choice is 3:
				self.twist_down(index)
			elif twist_choice is 4:
				self.twist_top_right(index)
			elif twist_choice is 5:
				self.twist_top_left(index)
			moves.append([twist_choice, index])
			twists -= 1
		return moves

	def unrandomize(self, moves):
		reverse_moves = []
		moves.reverse()
		for move in moves:
			if move[0] is 0:
				reverse_moves.append([1, move[1]])
				self.twist_left(move[1])
			elif move[0] is 1:
				reverse_moves.append([0, move[1]])
				self.twist_right(move[1])
			elif move[0] is 2:
				reverse_moves.append([3, move[1]])
				self.twist_down(move[1])
			elif move[0] is 3:
				reverse_moves.append([2, move[1]])
				self.twist_up(move[1])
			elif move[0] is 4:
				reverse_moves.append([5, move[1]])
				self.twist_top_left(move[1])
			elif move[0] is 5:
				reverse_moves.append([4, move[1]])
				self.twist_top_right(move[1])
		return reverse_moves

	def twist_right(self, row):
		self._swap_rows_rightward(row)
		if row is 0:
			self._turn_face_leftward(self.top)
		elif row is 2: 
			self._turn_face_rightward(self.bottom)

	def _swap_rows_rightward(self, row):
		face = self.faces
		temp = self.copy_face(face[self.front])
		self._replace_row(face[self.left], face[self.front], row)
		self._replace_row(face[self.back], face[self.left], row)
		self._replace_row(face[self.right], face[self.back], row)
		self._replace_row(temp, face[self.right], row)

	def twist_left(self, row):
		self._swap_rows_leftward(row)
		if row is 0:
			self._turn_face_rightward(self.top)
		elif row is 2:
			self._turn_face_leftward(self.bottom)

	def _swap_rows_leftward(self, row):
		face = self.faces
		temp = self.copy_face(self.faces[self.front])
		self._replace_row(face[self.right], face[self.front], row)
		self._replace_row(face[self.back], face[self.right], row)
		self._replace_row(face[self.left],face[self.back], row)
		self._replace_row(temp, face[self.left], row)

	def _replace_row(self, replacing_face, face_to_replace, row):
		index = row * 3
		face_to_replace[index] = replacing_face[index]
		face_to_replace[index + 1] = replacing_face[index + 1]
		face_to_replace[index + 2] = replacing_face[index + 2]

	def twist_up(self, col):
		self._swap_columns_upward(col)
		if col is 0:
			self._turn_face_leftward(self.left)
		elif col is 2:
			self._turn_face_rightward(self.right)

	def _swap_columns_upward(self, col):
		face = self.faces
		temp = self.copy_face(face[self.front])
		self._replace_col(face[self.bottom], face[self.front], col)

		face[self.bottom][col] = face[self.back][col + 6]
		face[self.bottom][col + 3] = face[self.back][col + 3]
		face[self.bottom][col + 6] = face[self.back][col]

		face[self.back][col] = face[self.top][col + 6]
		face[self.back][col + 3] = face[self.top][col + 3]
		face[self.back][col + 6] = face[self.top][col]

		self._replace_col(temp, face[self.top], col)

	def twist_down(self, col):
		self._swap_columns_downward(col)
		if col is 0:
			self._turn_face_rightward(self.left)
		elif col is 2:
			self._turn_face_leftward(self.right)

	def _swap_columns_downward(self, col):
		face = self.faces
		temp = self.copy_face(face[self.front])
		self._replace_col(face[self.top], face[self.front], col)

		face[self.top][col] = face[self.back][col + 6]
		face[self.top][col + 3] = face[self.back][col + 3]
		face[self.top][col + 6] = face[self.back][col]

		face[self.back][col] = face[self.bottom][col + 6]
		face[self.back][col + 3] = face[self.bottom][col + 3]
		face[self.back][col + 6] = face[self.bottom][col]

		self._replace_col(temp, face[self.bottom], col)

	def _replace_col(self, replacing_face, face_to_replace, col):
		face_to_replace[col] = replacing_face[col]
		face_to_replace[col + 3] = replacing_face[col + 3]
		face_to_replace[col + 6] = replacing_face[col + 6]

	def twist_top_right(self, row):
		self._swap_top_rightward(row)
		if row is 0:
			self._turn_face_rightward(self.back)
		elif row is 2:
			self._turn_face_rightward(self.front)

	def _swap_top_rightward(self, row):
		face = self.faces
		temp = self.copy_face(face[self.top])

		if row is 0:
			row_index = 0
			col_index = 0
		elif row is 2:
			row_index = 2 * 3
			col_index = 2
		else:
			row_index = 1 * 3
			col_index = 1

		self._col_to_row(face[self.left], col_index, face[self.top], row_index, True)

		# change indices for bottom to left
		if row is 0:
			row_index = 2 * 3
			col_index = 0
		elif row is 2:
			row_index = 0
			col_index = 2

		self._row_to_col(face[self.bottom], row_index, face[self.left], col_index, False)

		# change indices for right to bottom
		if row is 0:
			row_index = 2 * 3
			col_index = 2
		elif row is 2:
			row_index = 0
			col_index = 0

		self._col_to_row(face[self.right], col_index, face[self.bottom], row_index, True)

		# change indices for top to right
		if row is 0:
			row_index = 0
			col_index = 2
		elif row is 2:
			row_index = 2 * 3
			col_index = 0

		self._row_to_col(temp, row_index, face[self.right], col_index, False)

	def twist_top_left(self, row):
		self._swap_top_leftward(row)
		if row is 0:
			self._turn_face_leftward(self.back)
		elif row is 2:
			self._turn_face_leftward(self.front)

	def _swap_top_leftward(self, row):
		face = self.faces
		temp = self.copy_face(face[self.top])

		if row is 0:
			row_index = 0
			col_index = 2
		elif row is 2:
			row_index = 2 * 3
			col_index = 0
		else:
			row_index = 1 * 3
			col_index = 1

		self._col_to_row(face[self.right], col_index, face[self.top], row_index, False)

		if row is 0:
			row_index = 2 * 3
			col_index = 2
		elif row is 2:
			row_index = 0
			col_index = 0

		self._row_to_col(face[self.bottom], row_index, face[self.right], col_index, True)

		if row is 0:
			row_index = 2 * 3
			col_index = 0
		elif row is 2:
			row_index = 0
			col_index = 2

		self._col_to_row(face[self.left], col_index, face[self.bottom], row_index, False)

		if row is 0:
			row_index = 0
			col_index = 0
		elif row is 2:
			row_index = 2 * 3
			col_index = 2

		self._row_to_col(temp, row_index, face[self.left], col_index, True)

	def _col_to_row(self, col_face, col, row_face, row, reverse):
		if reverse:
			row_face[row] = col_face[col + 6]
			row_face[row + 1] = col_face[col + 3]
			row_face[row + 2] = col_face[col]
		else:
			row_face[row] = col_face[col]
			row_face[row + 1] = col_face[col + 3]
			row_face[row + 2] = col_face[col + 6]

	def _row_to_col(self, row_face, row, col_face, col, reverse):
		if reverse:
			col_face[col] = row_face[row + 2]
			col_face[col + 3] = row_face[row + 1]
			col_face[col + 6] = row_face[row]
		else:
			col_face[col] = row_face[row]
			col_face[col + 3] = row_face[row + 1]
			col_face[col + 6] = row_face[row + 2]

	def _turn_face_rightward(self, face):
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

	def _turn_face_leftward(self, face):
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

	def copy_face(self, face):
		temp = ["", "", "", "", "", "", "", "", ""]
		temp_index = 0
		for item in face:
			temp[temp_index] = face[temp_index]
			temp_index += 1
		return temp

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
