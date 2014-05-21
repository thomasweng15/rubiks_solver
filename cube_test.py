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

