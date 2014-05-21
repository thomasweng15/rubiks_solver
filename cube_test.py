from cube import Cube
import yaml

def compare(cube, test_states, state):
	passed = True
	face = 0
	while face < 6:
		cube_face = ''.join(cube.faces[face])
		test_face = test_states[state][face]
		if cube_face != test_face:
			print "Test failed on state '" + state + "'' on face " + str(face) + ":"
			print "cube: " + cube_face
			print "test: " + test_face
			passed = False
		face += 1

	if passed:
		print "test '" + state + "'' passed."

def test_face_twist(cube, test_states, numbered_faces, index):
	cube.twist_row_right(index)
	compare(cube, test_states, 'face_right_' + str(index))
	cube.load_faces(numbered_faces)

	cube.twist_row_left(index)
	compare(cube, test_states, 'face_left_' + str(index))
	cube.load_faces(numbered_faces)

if __name__ == '__main__':
	print "Testing Cube object."
	test_states_file = open("test_states.yaml", "r")
	test_states = yaml.safe_load(test_states_file)	
	cube = Cube()
	compare(cube, test_states, 'initial')
	
	count = 0
	while count < 3:
		cube.twist_row_right(count)
		compare(cube, test_states, 'right_' + str(count))
		cube.reset()

		cube.twist_row_left(count)
		compare(cube, test_states, 'left_' + str(count))
		cube.reset()

		cube.twist_col_up(count)
		compare(cube, test_states, 'up_' + str(count))
		cube.reset()

		cube.twist_col_down(count)
		compare(cube, test_states, 'down_' + str(count))
		cube.reset()

		count += 1

	indexed_faces = [
		["1", "2", "3", "4", "5", "6", "7", "8", "9"],
		["1", "2", "3", "4", "5", "6", "7", "8", "9"],
		["1", "2", "3", "4", "5", "6", "7", "8", "9"],
		["1", "2", "3", "4", "5", "6", "7", "8", "9"],
		["1", "2", "3", "4", "5", "6", "7", "8", "9"],
		["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	]

	cube.load_faces(indexed_faces)
	compare(cube, test_states, 'indexed_faces')

 	test_face_twist(cube, test_states, indexed_faces, 0)
 	test_face_twist(cube, test_states, indexed_faces, 2)

 	cube.twist_top_row_right(0)
 	compare(cube, test_states, 'top_row_right_0')
 	cube.load_faces(indexed_faces)

 	cube.twist_top_row_right(1)
 	compare(cube, test_states, 'top_row_right_1')
 	cube.load_faces(indexed_faces)

 	cube.twist_top_row_left(0)
 	compare(cube, test_states, 'top_row_left_0')
 	cube.load_faces(indexed_faces)

 	cube.twist_top_row_left(1)
 	compare(cube, test_states, 'top_row_left_1')
 	cube.load_faces(indexed_faces)
