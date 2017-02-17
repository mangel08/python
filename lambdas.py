# L A M B D A S

#Lambda nos sirve para poder crear pequeñas funciones anonimas, en una sola linea de codigo, esto se deberia usar para hacer cosas especificas

# suma(a, b):

	# return a + b

#declarando un lambda
#en lambda no se coloca el return ya que
#por defecto siempre retornan algo
mi_funcion = lambda a, b : a + b
				#valores : return

resultado = mi_funcion(50,40)
print(resultado)

formato = lambda sentencia : '¿{}?'.format(sentencia)

resultado = formato('Puedes hacer esto una pregunta')

print(resultado)

no_valor = lambda : 10

resultado = no_valor()
print(resultado)

#Si al lamda no se le asigna un valor a retornar da error, pero se puede mandar a ejecutar una accion por ejemplo print()
no_resultado = lambda : print('Deben de ejecutar una acción')

resultado = no_resultado()

