#Primera forma para llamar a un archivo
#import calculadora

# resultado = calculadora.suma(30,45)
# print(resultado)

#Segunda forma para llamar a un archivo
from calculadora import suma, resta as r1
# from calculadora import *
resultado = suma(30,45)
print(resultado)
resultado = r1(30,45)
print(resultado)

