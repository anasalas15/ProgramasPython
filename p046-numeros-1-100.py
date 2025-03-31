# Numeros del 1 al x usando ciclo for 

import os; os.system('clear')

x = int(input('Hasta donde ? '))
i = int(input('Incremento ? '))

for n in range(0,x + 1, i):
    print(n, end=' ')

print('\nLlegamos al final')

