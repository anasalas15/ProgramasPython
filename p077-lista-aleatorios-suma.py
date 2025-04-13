# Generar dos listas de 10 numeros aleatorios, sumar en una tercera lista solo si son impares

import random, os; os.system('cls')

print('Generar dos listas de 10 numeros aleatorios, sumar en una tercera lista solo si son impares ')

lista1 = []
lista2 = []
lista3 = []
MAX = 10

print('\nGenerando listas aleatorias')
for n in range(MAX):
    lista1.append( random.randint(1, 10) )
    lista2.append( random.randint(1, 10) )

print(f'Lista 1 : {lista1}')
print(f'Lista 2 : {lista2}')

print('\nSuma de numeros impares ')
for i in range(MAX):
    if lista1[i] % 2 !=0 and lista2[i] % 2 !=0:
        lista3.append( lista1[i] + lista2[i])

print(f'\nLista 3: {lista3}')