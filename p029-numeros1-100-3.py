#Imprime numeros de 1 a 100 

import os; os.system('clear')

n = int(input('Hasta donde? '))
d = int(input('Incrmentos ? '))

c = 1

while c <= n:
    print(c, end=' ')
    c += d
else:
    print('\nValor final de c=', c)

print('\nProceso terminado')