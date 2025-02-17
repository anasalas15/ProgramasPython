# Verificar si un numero es negativo, positivo o cero

import os;os.system('clear')

print('Verificar si un numero es negativo, positivo o cero\n')

n = int(input('Dame un numero entero: '))

if n > 0:
    print('El numero es positivo\n')
if n < 0:
    print('El numero es negativo\n')
if n == 0:
    print('El numero es cero\n')
    