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

class Mascota:
	nombre = "" #Todas las mascotas necesitan un nombre.

	def __init__(self,nombre):
		self.nombre = nombre

	def mostrar_nombre(self):
		print(self.nombre)


class Gato(Felino, Mascota): #clase hijo
	
	def __init__(self,nombre):
		Mascota.__init__(self,nombre)
		self.nombre_gato = nombre

	def gato_cazador(self):
		self.cazar()

	def mostrar_nombre(self): #Sobre escritura de metodos
		Mascota.mostrar_nombre(self)
		print("El nombre del gato es: {}".format(self.nombre))

gato = Gato('Tom')
# gato.nombre = "Tom"
gato.mostrar_nombre()


