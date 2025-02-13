# Calculo del volumen de un cilindro, dado su radio y altura 

import math as m 

print('Calculo del volumen de un cilindro, dado su radio y altura ')

radio  = float(input('Dame el radio: '))
altura = float(input('Dame la altura: '))

volumen = m.pi * (radio * radio) * altura

print(f'El volumen del circulo es: {volumen:.2f}')
