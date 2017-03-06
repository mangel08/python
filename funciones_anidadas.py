#Funcion normales

# def validacion (num_uno, num_dos):
# 	return num_uno > 0 and num_dos > 0

# def division(num_uno, num_dos):
# 	#LLamado de funciones
# 	if validacion(num_uno, num_dos): 
# 		return num_uno / num_dos

# resultado = division(10,0)
# print(resultado)

#Funcinoes anidadas

# def division(num_uno, num_dos):

# 	def validacion():
# 		return num_uno > 0 and num_dos > 0

# 	if validacion():
# 		return num_uno / num_dos

# resultado = division(10,0)
# print(resultado)

# F U N C I O N   C L O S U R E
def crear_funcion(num_uno, num_dos):
	def validacion():
		print("se ejecuta validacion")
		return num_uno > 0 and num_dos > 0

	return validacion
		

# nueva_funcion = crear_funcion(10,-5)
# print(nueva_funcion())

def aplicar_funcion (func):
	resultado = func()
	print(resultado)

nueva_funcion = crear_funcion(10,9)
aplicar_funcion(nueva_funcion)


