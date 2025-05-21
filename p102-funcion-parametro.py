# Ejemplificar el uso de parametros en una funcion 

import os

def saluda(nombre):
    print(f'\n Hola {nombre} bienvenido a las funciones en Python, tu nombre tiene {len(nombre)} caracteres')

os.system('cls')

print('\nMandando saludos desde la funcion\n')

saluda('Carlos Castaneda')
saluda('Ana Rosales')
saluda('Rocio Soto')

nombres = ['Hugo', 'Paco', 'Luis', 'Lucia']

#for s in range(5):
    #saluda(str(s)*5)

for nombre in nombres:
    saluda(nombres)


