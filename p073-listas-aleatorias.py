# Generar dos listas de numeros aleatorios y la suma en una tercera 

import os; os.system('cls')
import random

lista1 = []
lista2 = []
lista3 = []
MAX = 10

print('Generar dos listas de numeros aleatorios y la suma en una tercera ')

print('\nGenerando dos listas de numeros aleatorios')
for n in range(MAX):
    lista1.append( random.randint(1, 100) )
    lista2.append( random.randint(1, 100) )

print(f'Lista 1 : {lista1}')
print(f'Lista 2 : {lista2}')

print('\nLa suma de los cuadrados : ')
for i in range(MAX):
    lista1[i] = lista1[i]**2
    lista2[i] = lista2[i]**2
    lista3.append( lista1[i] + lista2[i])

print(f'Lista 1 : {lista1}')
print(f'Lista 2 : {lista2}')
print(f'Lista 3 : {lista3}')