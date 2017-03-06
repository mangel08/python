def generador(*args):
	"""Recibe n cantidad de numeros y regresa el numero
	ademas de regresar True o False si el numero es mayor a 5
	"""
	for valor in args:
		yield valor, True if valor > 5 else False

nombre = generador.__name__
documentacion = generador.__doc__

print(nombre, ":")
print(documentacion)

