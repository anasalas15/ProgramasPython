#Calcular el area de un circulo

import math

print('Calculando el area de un circulo')

radio = float( input('Dame el radio del circulo ? ') )

# area = 3.1416 * radio * radio 
area = math.pi *math.pow(radio,2)

print(f'El circulo de radio {radio} tiene el area de {area:,.2f}')

