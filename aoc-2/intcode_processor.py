from input import opcode


def intcode_processor(index=0):
	new_index = opcode[index+3]
	pos2 = opcode[index+1]
	pos3 = opcode[index+2]

	if opcode[index] == 99:
		return
	if opcode[index] == 1:
		new_val = opcode[pos2] + opcode[pos3]
	if opcode[index] == 2:
		new_val = opcode[pos2] * opcode[pos3]

	opcode[new_index] = new_val

	intcode_processor(index+4)

		



intcode_processor()
print(opcode)

def opcode_looper():
	global base_opcode
	global opcode
	opcode = base_opcode.copy()
	for x in range(1, 100):
		if opcode[0] == 19690720:
			return
		for y in range(1, 100):	
			if opcode[0] == 19690720:
				return x, y
			opcode = base_opcode.copy()		
			opcode[1] = x
			opcode[2] = y
			opcode_processor()



# opcode_looper()	
