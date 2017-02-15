my_list = ["string", 15, 15.6, True]

#Insertar al final
print("Metodo Insert al final \n")
my_list.append(6)
print(my_list \n)

#Insertar
print("Metodo Insert especificando posición \n")
my_list.insert(1, "insert")
print(my_list \n)

#Remover mediante el valor
print("Metodo Remove \n")
my_list.remove(15)
print(my_list \n)

#Remover el ultimo valor de la lista y lo retorna pop()
print("METODO Array.pop() \n")
#antes
print("Antes")
print(my_list \n)

#despues

last_value = my_list.pop()
print("Despues")
print(my_list \n)
print(last_value \n)

#Metodo de ordenamiento de listas sort

my_list2 = [1,9,22,6,8,65,14,99]

#ascendente
my_list2.sort()
print("Metodo Array Sort Asc \n")
print(my_list2 \n)
#descente
my_list2.sort(reverse = True)
print("Metodo Array Sort Desc \n")
print(my_list2 \n)

# Metodo para unir arreglos

my_list_one = [1,9,22,6,8,65,14,99]
my_list_two = [22, 23]

# Extend une los 2 arreglos en 1 solo
my_list_one.extend(my_list_two)
print("Metodo Array extend \n")
print(my_list_one)

# Append une en la ultima posición del 1er arreglo y toma cualquier tipo de dato en este caso inserto en la ultima posición todo el arreglo 2
my_list_one.append(my_list_two)
print("Metodo Array append array \n")
print(my_list_one)