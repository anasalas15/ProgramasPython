#Funcion que procesa un numero entre 1 y 4 y regresa una estacion con letra 

import os 

def estacion(n):
    if n==1: est='Primavera'
    elif n==2: est='Verano'
    elif n==3: est='Otoño'
    elif n==4: est='Invierno'
    return est

os.system('cls')

while True:
    n = int(input('Estacion (1..4) ? '))
    if n>=1 and n<=4:
        break

print(f'\nLa estacion es {estacion(n)}')