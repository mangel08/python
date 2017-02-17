diccionario = { 'a' : 55, 'b' : True, 5 : "esto es un string", (1,2): False, 'a' : False}

# Creando nuevo registro
diccionario['c'] = 'nuevo string' #creariamos clave/valor

# Modificando el valor de clave a
diccionario['a'] = True

#accendiendo a un valor
valor = diccionario['c']

#accediendo a un valor mediante get()
#tiene 2 parametros uno es la llave para obtener el valor, el 2do parametro es un valor que se define por si la llave introducida no existe en el diccionario
valor = diccionario.get('z', False)

# Para borrar un valor de un diccionario

del diccionario[5] #eliminar por la llave

print(diccionario)
print(valor)

# Para obtener las keys de un diccionario usar metodo keys()
llaves = diccionario.keys() #retorna un objeto iterable con los keys

llaves = list(diccionario.keys()) #retorna un arreglo con los keys

valores =tuple( diccionario.values())

#Creciendo el diccionario

#1era forma
diccionario_dos = {'z':23, 'w': 88}

diccionario['z'] = diccionario_dos['z']
diccionario['w'] = diccionario_dos['w']

#2da forma RECOMENDADA
diccionario.update(diccionario_dos)#El que queremos que incremente

print(llaves)
print(valores)

