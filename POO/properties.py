class Usuario:

	#Metodo Constructor
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password) #__atributo es un atributo private
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	# GET
	@property
	def password(self):
		return self.__password

	# SETTER
	@password.setter
	def password(self, valor):
		self.__password = self.__generar_password(password)


user = Usuario('miguel', 'miguel23', 'mangel.2711@gmail.com')

print(user.password)
user.password = 'Nuevo password'
print(user.password)