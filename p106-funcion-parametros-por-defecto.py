#Ejemplifica el uso de parametros con valores por defecto

import os

def saluda(nombre='Nadie', edad=0):
    print(f'\nHola {nombre}, tienes una edad de {edad}')

os.system('cls')

print('\Invocar una funcion con un numero distinto de parametro')

saluda('Luis')
saluda()
saluda('Luis', 25)