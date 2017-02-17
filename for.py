lista = (1,2,3,4,5,6,7,8,9,10)

for valor in lista: 
	# print(valor)
	pass


nuevo_rango = range(10,20,2)

for valor in nuevo_rango:
	# print(valor)
	pass

#recorriendo una lista obteniendo su valor y obteniendo sus indices mediante una variable externa igualada a 0 y incrementandola al final de cada iteración

indi = 0
for valor in lista:
	"""
	print(valor, 'tiene el indice: ', indi)
	indi +=1
	"""
	pass

#recorriendo una lista por obteniendo el valor y sus indices mediante la funcion enumerate()
for indice, valor in enumerate(lista):
	# print(valor, 'tiene el indice: ', indice)
	pass

#recorriendo con un rango hasta el final de una lista
for valor in range(0, len(lista)):
	pass #print(valor)

#recorriendo un string
for valor in 'Curso de Código facilito':
	pass #print(valor)

diccionario = {'a': 10, 'b': 20, 'c': 500}

#recorriendo un diccionario por sus items llave/valor
for key,valor in diccionario.items():
	pass #print('Llave: ', key, ' tiene el valor de ', valor)

#recorriendo un diccionario por sus llaves
for key in diccionario.keys():
	pass #print('Llaves: ', key)

#recorriendo un diccionario por sus valores
for valor in diccionario.values():
	print(valor)