class Usuario:
	#Metodo Constructor
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password) #__atributo es un atributo private
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	def get_password(self):
		return self.__password

user = Usuario('miguel', 'miguel', 'mangel.2711@gmail.com')

print(user.username)
# print(user.password)
print(user.email)
print(user.get_password())