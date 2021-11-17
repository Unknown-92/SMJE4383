input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

for line in input_file:
	new_str = ''
	line = line.strip()
	for char in line:
		new_str = char + new_str
	print(new_str, file = output_file)
	
	print('Line: {:12s} reversed is: {:s}'.format(line,new_str))
input_file.close()
output_file.close()
