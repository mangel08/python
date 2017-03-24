class Circulo:
	#Variable de clase es como una constante _variable para identificar que es una constante
	_pi = 3.1416

	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return self.radio * self.radio * Circulo._pi
		

print(Circulo._pi)
a = Circulo(4)
b = Circulo(3)

# print(a.pi)
# print(b.pi)

print(a.area())