# El usuario introduce nombres y edades, imprime mayores de edad y el de mayor edad

import os; os.system('cls')

print('El usuario introduce nombres y edades, imprime mayores de edad y el de mayor edad')

nombres = []
edades = []

while True:
    nombre = input('Nombre : ')
    if not nombre == '':
        nombres.append(nombre)
        edad = int(input('Edad : '))
        edades.append(edad)
    else:
        break

print(f'Nombres : {nombres}')
print(f'Edades : {edades}')

print('\nLos mayores de edad son : ')
for i in range( len(edades) ):
    if edades[i] >= 18:
        print(f'{nombres[i] - {edades[i]}}')

print('\nEl de mayor edad es: ')
me = max(edades)
pos = edades.index(me)
print(f'{nombres[pos]} - {edades[pos]}')
