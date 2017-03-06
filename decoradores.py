def decorador(func): #A,B

	def before_action():
		print("Vamos a ejecutar la funcion")

	def after_action():
		print("Se ejecuto la funcion")

	def nueva_funcion(*args, **kwargs):
		before_action()
		resultado = func(*args, **kwargs)
		after_action()
		return resultado

	return nueva_funcion #C

@decorador
def saluda():
	print("Hola Mundo")

#A, B, C son funciones
#A recibe como parametro B para poder crear C
#UN DECORADOR ES UNA FUNCION QUE CREA FUNCIONES
# saluda()

@decorador
def suma(a,b):
	return (a + b)

resultado = suma(80,17)
print(resultado)
# saluda()