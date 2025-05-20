# Muestra las operaciones basicas sobre conjuntos

import os; os.system('cls')

muns = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}

print('Ejmemplificando las operaciones basicas sobre conjuntos')

print(f'El conjunto: {muns} - {len(muns)}')

print('\nLista de municipios usando un ciclo')
for m in muns:
    print(m, end= '')

print('\nZacatecas esta en el conjunto de municipios: ', 'Zacatecas' in muns)

print('\nAgregar un elemento al conjunto')
muns.add('Teul')
print(f'El conjunto: {muns} - {len(muns)}')

print('\nAgregar varios elemntos a un conjunto')
otros = {'Luis Moya', 'Ojocaliente', 'Tepetongo'}
muns.update(otros)
print(f'El conjunto: {muns} - {len(muns)}')

print('\nEliminar elementos de un conjunto')
muns.remove('Zacatecas') #Genera error si no existe el elemento
muns.discard('Ojocaliente') #Si el elemnto no existe no genera error
muns.pop() # Elimina el primer elemento del conjunto
print(f'El conjunto: {muns} - {len(muns)}')

print('\nEliminar todos los elementos de un conjunto')
muns.clear()
print(f'El conjunto: {muns} - {len(muns)}')