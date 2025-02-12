# Ejemplifica las operaciones matematicas basicas

import os;os.system('clear')

# datos de prueba
x = float(input('Valor de x ?'))
y = float(input('Valor de y ?'))

suma  = x + y
resta = x - y
mult  = x * y
div   = x / y 
res   = x % y 
pot   = x ** y
dive  = x // y 

print(f'Suma : {suma}\nResta : {resta}\nMultiplicacion : {mult}\nDivision : {div} ')
print(f'Residuo : {res}\nPotencia : {pot}\nDivision Entera : {dive}')
