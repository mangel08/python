import random

valor = random.randint(0,10)
print(valor)

lista = [True, "Strings", 23, False]

valor = random.choice(lista)
print(valor)

print(lista)
random.shuffle(lista)
print(lista)