#Ejemplificar el uso de una funcion que recibe varios parametros 

import os

def cuadro(r,c, car):
    for i in range(1, r+1):
        for j in range(1, c+1):
            print(car, end='')
        print()

os.system('cls')
print('Creando u cuadro de r x c del caracter deseado')
r = int(input('Renglones: '))
c = int(input('Columnas: '))
car = input('Caracter: ')
cuadro(r, c, car)