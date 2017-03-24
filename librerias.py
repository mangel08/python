import random, datetime, sys, time

# valor = random.randint(0,10)
# print(valor)

# lista = [True, "Strings", 23, False]

# valor = random.choice(lista)
# print(valor)

# print(lista)
# random.shuffle(lista)
# print(lista)

# print(datetime.datetime.now())

for i in range(100):
	time.sleep(0.5)
	sys.stdout.write("\r%d %%" % i)
	sys.stdout.flush()

