class Animal:
	@property
	def terrestre(self):
		return True

class Felino(Animal): #Clase padre
	@property
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El felino esta cazando")

class Gato(Felino): #clase hijo
	def gato_cazador(self):
		self.cazar()

class Jaguar(Felino): #clase hijo
	pass

gato = Gato()
jaguar = Jaguar()

print(gato.terrestre)
print(jaguar.terrestre)
print(gato.gato_cazador())
print(jaguar.garras_retractiles)