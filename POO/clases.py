class Lapiz:
	#Atributos
	color = 'Amarillo'
	contiene_borrador = False
	usa_grafito = True

	#Metodos
	def dibujar(self):
		print("El lapiz esta dibujando.")

	def borrar(self):
		if self.es_valido_para_borrar():
			print("El lapiz esta borrando")
		else:
			print("NO es posible borrar")

	def es_valido_para_borrar(self):
		return self.contiene_borrador

	def setBorrador(self, borrador):
		self.contiene_borrador = borrador

#Esto es un objeto Lapiz
lapiz_generico = Lapiz()

print(lapiz_generico.color)
print(lapiz_generico.contiene_borrador)
print(lapiz_generico.usa_grafito)

lapiz_generico.dibujar()
lapiz_generico.setBorrador(False)
lapiz_generico.borrar()



