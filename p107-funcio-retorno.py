#Ejemplificar el uso de valores de retorno de la funcion

import os

def suma(n1, n2):
    s = n1 + n2
    return s

os.system('cls')
print('\nInvocando a una funcion con dos parametros, y recibiendo el valor de retorno')

res = suma(10, 20) #guardamos el resultado en una variable
print(f'\nEl resultado de la suma es {res}')

print('\nDame dos numeros enteros y te caluculare la suma: ')
a, b = int(input()), int(input()) #leo los valores en variables que se llamen diferentes a los parametros, es valido
print(f'\nLa suma de los numeros que me diste es {suma(a,b)}')
