fruta = 'manzana'
# fruta = 'kiwi'

if fruta == 'kiwis':
	print('Condicion')
	print("El valor es kiwi")

elif fruta == 'manzana':
	#print('Es una manzana')
	pass
elif fruta != 'kiwis':
	print("Es diferente")

else:
	print('Else')
	print('No son iguales')

mensaje = 'El valor es kiwi' if fruta == 'kiwi' else 'No son iguales'
print(mensaje)

valor = 1
valor_dos = 20

#operador lógico and
if valor and valor_dos > 20 :
	print('Es verdad')
else:
	print('No es verdad')

#operador lógico or
if valor or valor_dos > 20 :
	print('Es verdad')
else:
	print('No es verdad')


