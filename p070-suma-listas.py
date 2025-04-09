# Suma dos listas de n numeros introducidas por el usuario

import os; os.system('cls')

print('\nSumar los elementos de dos listas ')

lista1 = []
lista2 = []
lista3 = []
MAX = 4 
n = 0

print('\nLeyendo los elementos de la lista 1 ')
for i in range(MAX):
    n = int(input(f'Lista1[{i+1}]= '))
    lista1.append(n)

print(f'Lista 1 : {lista1}')


print('\nLeyendo los elementos de la lista 2 ')
for i in range(MAX):
    n = int(input(f'Lista2[{i+1}]= '))
    lista2.append(n)

print(f'Lista 2 : {lista2}')

for i in range(MAX):
    lista3.append( lista1[i] + lista2[i] )

print(f'\nLista 3 : {lista3}')


