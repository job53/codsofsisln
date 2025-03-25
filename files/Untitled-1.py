with open('alumnos.txt', 'r') as fichero:
	for line in fichero.readlines():
		print(line, end='')