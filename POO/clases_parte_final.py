class Usuario:
	def __new__(cls):
		print('Este metodo es el primero que se ejecuta')
		return super().__new__(cls)		

	def __init__(self):
		# self.__password = 'Este es un secreto'
		print('Este metodo es el segundo que se ejecuta')
	
	def mostrar_password(self):
		print(self.__password)

	def __str__(self):
		return "Esto se imprime cuando intento mostrar el objeto"

	def __getattr__(self, nombre):
		print("Aqui mostramos que no se encontro el atributo")
		self.otros_metodos()

	def otros_metodos(self):
		print("otro metodo")
		
usuario = Usuario()
print(usuario)
print(usuario.apellido)
# usuario.nombre = "Miguelangel"
# print(usuario.nombre)
# print(usuario.__dict__)

# usuario.__password = 'Este ya no es un secreto'
# print(usuario.__dict__)
# usuario.mostrar_password()
