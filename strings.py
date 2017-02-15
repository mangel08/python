# VARIABLES SE DECLARAN EN MINUSCULAS NO PUEDE TENER NINGUNA MAYUSCULA

#    S T R I N G S

name = "Miguel"
name2 = "Roger"
lastname = "Palma"
message = name + " " + lastname
message2 = "Hola me llamo " + name + " " + lastname
message3 = "Hola %s mi nombre es %s %s" %(name2,name,lastname)

print(name)
print(lastname)
print(name + lastname)
print(message)
print(message2)
print(message3)


#     L I S T A S  D E  S T R I N G S

my_string = "Curso de Código Facilito!"
print(my_string)
print(my_string[0])
print(my_string[16])
print(my_string[-1]) #Accediendo a los caracteres desde la derecha
print(my_string[0:16])
print(my_string[-2:-1])
print(my_string[0:10:2]) #SALTO DE CHAR EN ESTE CASO 1 SI 1 NO

print(my_string[::-1]) #ESO ES UN REVERSE PERMITE LEER EL STRING DE DERECHA A IZQUIERDA


#    M E T O D O S  D E  S T R I N G S 

course = 'Curso'
my_string = 'Código Facilito!'

"""METODOS DE FORMATO"""
result = '{} de {}'.format(course, my_string)

print(result)

result2 = '{a} de {b}'.format(b = course, a =my_string)

print(result2)

# LOWERCASE
result = result.lower()
print(result)

#UPPERCASE
# result = result.upper()
# print(result)

#STRING COMO TITULO
# result = result.title()
# print(result)

"""M E T O D O S  D E  B U S Q U E D A"""

pos = result.find('código')
print(pos)

count = result.count('c')
print(count)

new_string = result.replace('c', 'x')
new_string = result.split(' ')
print(new_string)