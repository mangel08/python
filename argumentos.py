
def suma(*args):
	print(args)
	print(type(args)) #Funcion type para sabe que tipo de dato es una variable

	# El asterisco (*) sirve para declarara en la funcion que puede tener 1 o n argumentos que luego esas argumentos estaran almacenados en una tupla ()

	resultado = 0
	for valor in args:
		resultado = resultado + valor
	return resultado

resultado = suma(1,2,3,4,5,6,7,8,9)
print(resultado)



def suma2(**kwargs):
	# print(argumento)
	# print(type(argumento)) #Funcion type para sabe que tipo de dato es una variable

	#El asterisco (*) sirve para declarara en la funcion que puede tener 1 o n argumentos 

	print(kwargs)
	valor = kwargs.get('valor23', 'No contiene el valor')
	print(valor)

	"""
	* -> n valores -> tuplas
	** -> n valores -> diccionarios
	"""

resultado = suma2(valor = 'hola', x = 2, y = 9, z = True)
print(resultado)