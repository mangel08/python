# try:
# 	print(2/0)
# except ZeroDivisionError as ex:
# 	print(ex)
# 	print("No es posible dividir por 0")

# print("Se termino el script")

try:
	lista = [1,2]
	print(lista[9])
except Exception as e:
	print(e)
	print("No se que paso, pero paso algo mal")
finally:
	print("se termino el script")
