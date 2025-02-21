# Verificar si la suma de dos numero enteros es igual a un tercer

import os; os. system('clear')

print('# Verificar si la suma de dos numero enteros es igual a un tercer ')

print('Dame 3 nueros enteros separados por <Enter> ')
n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3:
    print('\nLa suma de los dos primeros numero es igual al tercero')
else:
    print('\nLa suma de los dos primeros numeros no es igual al tercero ')

print('\nGracia por usar el programa')
