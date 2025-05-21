# Suma un rango de numeros consecutivo con una funcion
import os

def suma_rango(i, f):
    s = 0 
    for i in range(i, f+1):
        s = s + i
    return s

os.system('cls')
print('Dame un rango de valores consecutivos y te regreso la suma')

while True:
    i = int(input('Inicio: '))
    f = int(input('Fin: '))
    if i<f : break

r = suma_rango(i, f)
print(f'\nLa suma del rango {i}...{f} es {r}')
