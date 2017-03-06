"""   
Un Generador sirve para poder crear objetos
sin necesidad de almacenarlos en la memoria ram

"""
def generador(*args):
	for valor in args:
		yield valor * 10, True

for valor1, valor2 in generador(1,2,3,4,5,6,7,8,9):
	print(valor1, valor2)

