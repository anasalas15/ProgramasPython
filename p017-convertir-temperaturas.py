# Convertir temperaturas de farenheit a centigrados y viceversa 

import os; os.system('clear')

print('Convertir temperaturas de farenheit a centigrados y viceversa ')
print('De centrigados a farenheit..... [ 1 ] ')
print('De farenheit a centigrados..... [ 2 ] ')
op = int(input('Elige: '))


if op==1:
    print('Convirtiendo Centigrados a Farenheit .....')
    temp = float(input('Grados Centigrados ? '))
    res = ( temp * 9 / 5 ) + 32
    print(f'{temp} grados centigrados, equivale a {res} grados farenheit')
else:
    print('Convirtiendo Farenheit a Centigrados.....')
    temp = float(input('Grados Frenheit ? '))
    res = ( temp - 32 ) * 5 / 9
    print(f'{temp} grados farenheit, equivale a {res} grados centigrados')
    



