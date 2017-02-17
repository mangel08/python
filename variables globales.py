def palindromo(frase):
	frase = frase.replace(' ','') #Variables Locales
	return frase == frase[::-1]

frase = 'anita lava la tinas' #Variables Globales
resultado = palindromo(frase)
print(resultado)

def valor_global():
	#palabra reservada global para usar la variable global en una funcion
	global variable_global
	variable_global = 'Cambiar valor'

def mostrar_global():
	print(variable_global)

def crear_global():
	global nueva_variable
	nueva_variable = 'Esto es una variable global creada'

# variable_global = 'Esto es una variable globa'
# mostrar_global()
# valor_global()
# print(variable_global)

crear_global()
print(nueva_variable)