#Imprime numeros de 100  1 

import os; os.system('clear')

n = int(input('Desde donde? '))
d = int(input('Decrementos? '))
c = n

while c >= 1:
    print(c, end=' ')
    c -= d
else:
    print('\nValor final de c', c)

print('\nProceso terminado')