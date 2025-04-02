# Calcular el factorial m numeros enteros

import os;
os.system('clear')

print('Calcular el factorial m numeros enteros')

m = int(input('Hasta que numero deseas el factorial ? '))

for x in range(1, m+1):
    f = 1 
    sec = ""

    for i in range (1, x+1):
        f = f * i
        sec = sec + str(i) 
        if i < x :
            sec = sec + " * "

    print(f'{x}! = {sec} = {f:,}')