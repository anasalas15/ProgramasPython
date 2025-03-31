# Numeros del x al 0 usando ciclo for 

import os; os.system('clear')

x = int(input('Desde donde ? '))
i = int(input('Decremento ? '))

for n in range(x, 0, -i):
    print(n, end=' ')

print('\nLlegamos al final')