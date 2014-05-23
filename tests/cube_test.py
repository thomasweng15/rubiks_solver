from nose import with_setup
from ..cube import Cube
import yaml

def setup_function():
	global test_states
	global cube
	global indexed_faces

	indexed_faces = [
		["000", "001", "002", "010", "011", "012", "020", "021", "022"],
		["100", "101", "102", "110", "111", "112", "120", "121", "122"],
		["200", "201", "202", "210", "211", "212", "220", "221", "222"],
		["300", "301", "302", "310", "311", "312", "320", "321", "322"],
		["400", "401", "402", "410", "411", "412", "420", "421", "422"],
		["500", "501", "502", "510", "511", "512", "520", "521", "522"],
	]

	test_states_file = open("tests/cube_states.yaml", "r") # TODO make this variable
	test_states = yaml.safe_load(test_states_file)	
	cube = Cube()
	reset(cube, indexed_faces)

def reset(cube, faces):
	cube.load_faces(faces)

def compare(cube, test_states, state):
	face = 0
	while face < 6:
		cube_face = ' '.join(cube.faces[face])
		test_face = ''.join(test_states[state][face])
		assert cube_face == test_face, \
			"Test failed on state '" + state + "'' on face " + str(face) + ":" \
			+ "\ncube: " + cube_face \
			+ "\ntest: " + test_face
		face += 1

@with_setup(setup_function)
def test_initial_state():
	compare(cube, test_states, 'initial')

@with_setup(setup_function)
def test_single_twist_every_direction():
	count = 0
	while count < 3:
		cube.twist_row_right(count)
		compare(cube, test_states, 'right_' + str(count))
		reset(cube, indexed_faces)

		cube.twist_row_left(count)
		compare(cube, test_states, 'left_' + str(count))
		reset(cube, indexed_faces)

		cube.twist_col_up(count)
		compare(cube, test_states, 'up_' + str(count))
		reset(cube, indexed_faces)

		cube.twist_col_down(count)
		compare(cube, test_states, 'down_' + str(count))
		reset(cube, indexed_faces)

		count += 1

