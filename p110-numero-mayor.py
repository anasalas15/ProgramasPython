#Ejemplificar el uso de una funcion que recibe 3 parametros y cual es el mayor

import os

def mayor(c1, c2, c3):
    if c1>c2 and c1>c3:
        may = c1
    elif c2>c1 and c2>c3:
        may = c2
    elif c3>c1 and c3>c2:
        may = c3
    return may

os.system('cls')
print('Dame tres calificaciones y te dire cual es la mayor ')
a, b, c = float(input()), float(input()), float(input())
m = mayor(a, b, c)
if m ==0:
    print('Error: no hay numero mayor ')
else:
    print(f'El numero mayor es {m}')

