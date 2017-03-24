import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("Es necesario colocar por lo menos un argumento")
	else:
		if(sys.argv[1] == 'help'):
			print("puedes contactar a codigo facilito si tienes alguna duda")
		print(sys.argv[1])

	print(sys.argv)