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

	def mostrar_nombre(self):
		print(self.nombre)

class Mascota:
	nombre = "" #Todas las mascotas necesitan un nombre.



class Gato(Felino, Mascota): #clase hijo
	def gato_cazador(self):
		self.cazar()


gato = Gato()
gato.nombre = "Tom"
gato.mostrar_nombre()
# print(gato.terrestre)

