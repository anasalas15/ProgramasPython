# Simular un registro de calificaciones usando un diccionario, sacamos el promiedio
#Realizamos cambios y actualizaciones

import os ; os.system('cls')

materias = ['fisica','quimica','matematicas','geografia','estadistica']
califs = [10,9,8,7.5,6]
print(f'Lista de materias: {materias} - {len(materias)}')
print(f'Lista de calificaciones: {califs} - {len(califs)}')

notas= dict(zip(materias,califs))

print(f'\nEl diccionario completo de notas es {notas} - {len(notas)}')

#agregar
notas.update({'ingles':10,'programacion':7})
print(f'\nEl diccionario de notas es {notas} - {len(notas)}')

#remover
notas.pop('fisica')
notas.popitem()
print(f'\nEl diccionario completo de notas es {notas} - {len(notas)}')

#modificar
notas['quimica']=10
notas.update({'matematicas':10})
print(f'\nEl diccionario completo de notas es {notas} - {len(notas)}')

#mostrar la lista de materias y calificaiones asi como el promedio
s = 0
print(f'Matarias y calificaciones')
for m, c in notas.items():
    print(f'{m:<12} -{c:5}')
    s=s+c
p=s/len(notas)

print(f'La suma es {s} el promedio es {p}')

#limpear
notas.clear()
print(f'\nEl diccionario completo de notas es {notas} - {len(notas)}')