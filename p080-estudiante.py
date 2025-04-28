# Ejemplo de uso de un diccionario

import os ; os.system('cls')

estudiante = {
    'nombre':'juan perez',
    'edad':45,
    'email':'jperez@msn.com',
    'carrera':'sistemas'
    }
estudiante2 = {'nombre':'maria juarez','edad':35,'email':'maria@msn.com','carrera':'ingenieria','calificacion':9}
print(f'El diccionario:{estudiante},elementos{len(estudiante)}')

#modificar/ agregar
estudiante['Calificacion']= 9.5 # se agrega por que no exixte
estudiante['email']= 'juanp@gmail.com' # se modifica por que ya existe
print(f'\nEl diccionario:{estudiante},elementos{len(estudiante)}')

#iterar
print('\n Iterar por llaves:')
for k in estudiante.keys():
    print(k)

print('\nIterar por los valores:')
for v in estudiante.values():
    print(v)

print('Llaves y valores a la vez')
for k, v in estudiante.items():
    print(f'{k:<13} : {v}')

print(f'suma de las edades: {estudiante['edad'] + estudiante2['edad']}')

print(f'Promedio de calificaciones: {(estudiante['Calificacion'] + estudiante2['calificacion'])/2}')