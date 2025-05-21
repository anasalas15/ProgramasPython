#Ejemplificar el uso de una funcion con dos parametros

import os

def tabla(t,n):
    for i in range(1, n + 1):
        print(f'{t} x {i} = {t*i}')

os.system('cls')

print('Imprimiendo una tabla que tu decidas, hasta donde decidas')
t = int(input('Que tabla ? '))
n = int(input('Hata donde ? '))
tabla(t,n)

