#Imprime numeros de 100  1 

import os; os.system('clear')

n = int(input('Hasta donde? '))
c = n

while c >= 1:
    print(c, end=' ')
    c -= 1
else:
    print('\nValor final de c', c)

print('\nProceso terminado')