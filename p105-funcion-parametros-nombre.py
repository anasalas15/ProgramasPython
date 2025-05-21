# Ejemplifica el uso de nombres en los parametros
# esto permite invocar a la funcion co los parametros en el orden deseado

import os

def saluda(apaterno, amaterno, nombre):
    print(f'\nHola {apaterno} {amaterno} {nombre} bienvenido a esta Universidad')

os.system('cls')

print('\nInvocar una funcion usando los nombres de los parametros')

saluda('Castaneda', 'Ramirez', 'Carlos')

saluda('Carlos', 'Ramirez', 'Cataneda') #los parametros llegan a la funcion en orden incorrecto

saluda(nombre='Carlos', amaterno='Ramirez', apaterno='Castaneda')

