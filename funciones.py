#Funcion para calcular el factorial	

def factorial_numero(numero):
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero -=1
	# print(factorial)
	return factorial

result = factorial_numero(4)
# print(result)
					
result = factorial_numero(5)
# print(result)

result = factorial_numero(6)
# print(result)

def suma(a,b,c):
	return a + b + c

resultado = suma(10,20,30)
# print(resultado)

def division(a,b):
	return a / b

# Usando el orden de los argumentos
resultado = division(100,10)

# Usando los parametros para no usar el orden
resultado = division(b = 10, a = 100)
# print(resultado)


def multiplicacion(a, b = 10): #Utiliza el valor por defecto si y solo si no se coloca el valor al llamar a la funcion
	return a * b

resultado = multiplicacion(6)
# print(resultado)



#Una funcion en python puede retornar múltiples valores separando con comas retornando los valores en una tupla

def multiples_valores():
	return "String", 1, True, 25.6

mi_variable = multiplicacion
resultado = mi_variable(6,8)
print(resultado)

# string, entero, bol, floa = multiples_valores()

# print(string)
# print(entero)
# print(bol)
# print(floa)

# FUNCION QUE TOMA COMO ARGUMENTO OTRA FUNCION COMO PARAMETRO
def mostrar_resultado( funcion ):
	print(funcion(6,8))

mi_variable = division
mostrar_resultado( mi_variable )
