# Dados los anguos de un triangulo, calcular el 3er angulo

import os;os.system('clear')

print('Dados los anguos de un triangulo, calcular el 3er angulo')

angulo1 = int(input('Dame el primer angulo: '))
angulo2 = int(input('Dame el segundo angulo: '))

angulo3 = int(180 - (angulo1 +angulo2))

print(f'El tercer agulo del triangulo es: {angulo3}')
