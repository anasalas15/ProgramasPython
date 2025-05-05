# Procesar una lista de estudiantes usando una lista de diccionarios 
# Se calcula la suma de los promedios y el promedio general del grupo 

import os; os.system('cls')

grupo = [
    {'nombre':'Carlos','edad':45,'carrera':'Sistemas','promedio':9},
    {'nombre':'Rocio','edad':35,'carrera':'Sistemas','promedio':10},
    {'nombre':'Jose','edad':30,'carrera':'Electronica','promedio':8}
]

print(f'Grupo completo {grupo} - {len(grupo)}')

while True:
    print('\nDame los datos del estudiante')
    datos = {}
    nombre = input('Nombre ? ')
    if nombre != '':
        datos['nombre'] = nombre
        datos['edad'] = int(input('Edad: '))
        datos['carrera'] = input('Carrera: ')
        datos['promedio'] = float(input('Promedio: '))
        grupo.append(datos)
    else : break 

print(f'Grupo completo {grupo} - {len(grupo)}')


#Imprimir una tabla con los datos de los autos
print('\nDatos de los estudiantes en forma de tabla\n')

#Imprimir los encabezados 
print('-'*50)
for llave in grupo[0].keys():
    print(f'{llave:<12}', end='')
print()
print('-'*50)

#Imprimir cada dato de cada alumno 
for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<12}', end='')

    print()
print('-'*50)

suma = 0 
for alumno in grupo:
    suma = suma + alumno['promedio']

print(f'La suma del promedio es: {suma}')
print(f'El promedio del grupo : {suma / len(grupo)}')