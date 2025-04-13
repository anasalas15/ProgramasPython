# Leer n notas hasta introducir un 0, las notas pueden estar entre 0 y 100

import os; os.system('cls')

print('Procesamiento de notas ')

notas = []
mp = []
suma = prom = 0
n = -1

while n != 0:
    n = int(input('Dame las notas desde 0 a 100 ? '))
    if n > 0 and n <= 100:
        notas.append(n)
    else: print('>')

notas.sort()

suma = sum(notas)
prom = suma / len(notas)

for n in notas:
    if n < prom:
        mp.append(n)

print('\nProcesamiento')
print(f'Las notas son : {notas}')
print(f'Se introdujeron {len(notas)} notas')
print(f'La suma es : {suma}')
print(f'El promedio es : {prom}')
print(f'Las notas menores al promedio son: {mp} y son: {len(mp)}')
print(f'La nota minima es: {min(notas)}')
print(f'La nota maxima es: {max(notas)}')


