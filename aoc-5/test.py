from input import nums

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