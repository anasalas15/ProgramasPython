# Ejemplificar el uso de una funcion que recibe mas de 1 parametro

import os

def saluda(apaterno, nombre, edad):
    print(f'\nHola {apaterno} {nombre} tienes una edad de {edad}')

os.system('cls')

print('\nInvocando una funcion con mas de 1 parametro')

saluda('Rosales','Ana', 25)
#saluda('Soto') #se genera un error faltan parametros 
#saluda('Ruiz', 'Julia', 24, 10) #Se genera un error sobran parametros 

