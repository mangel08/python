class Circulo:
	#Variable de clase es como una constante _variable para identificar que es una constante
	# _pi = 3.1416

	def __init__(self, radio):
		self.radio = radio

	#Metodo estaticos
	@staticmethod
	def pi():
		return 3.1416

	#Metodos de instancia
	def area(self): 
		return self.radio * self.radio * self.pi()
		

print(Circulo.pi())
a = Circulo(7)
print(a.area())