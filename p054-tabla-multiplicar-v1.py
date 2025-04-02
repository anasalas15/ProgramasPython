# Tabla de multiplicar con for 

import os;
os.system('clear')

t = int(input('Que tabla ? '))
n = int(input('Hata donde ? '))

while(True):
    for i in range (1, n+1):
        print(f"{t} x {i} = { t * i }")

    if input('\nDeseas continuar (S/N)? ').upper()=='N':
        break

print('\Hemos llegado al final ...') 