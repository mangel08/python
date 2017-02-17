
"""
Metodo para llenar una lista comun y corriente
lista = []
for valor in range(0, 101):
	lista.append(valor)
"""

#Metodo de llenar listas, tuplas y diccionarios con ListComprehension

lista = [valor for valor in range(0,101) if valor % 2 == 0]

#Reglas para las List Comprehension
#1- valor a agregar a lista
#2. un ciclo.

tupla = tuple ( (valor for valor in range(0,101) if valor % 2 != 0))

diccionario = { indice:valor for indice, valor in enumerate(lista) if indice < 10}

print(lista)
print(tupla)
print(diccionario)