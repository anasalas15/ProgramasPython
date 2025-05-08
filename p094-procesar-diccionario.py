# Se tiene los datos de nombres y sueldos de los siguientes empleados, en dos listas

import os; os.system('cls')

Nombres = ['Juan','Pedro','Manuel','Elias','Maria','Felipe','Julia','Roberto']
Sueldos = [4550.22,8456.88,1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

print(f'Lista de Nombres: {Nombres} - {len(Nombres)}')  
print(f'Lista de Sueldos: {Sueldos} - {len(Sueldos)}')

restaurante = dict(zip(Nombres,Sueldos))

print(f'\nEl diccionario completo de empleados es {restaurante} - {len(restaurante)}')

# iteramos el diccionario
print('\nIterar por llaves:')
for k in restaurante.keys():
    print(k)
print('\nIterar por los valores:')
for v in restaurante.values():
    print(v)
print('\nLlaves y valores a la vez')
for k, v in restaurante.items():
    print(f'{k:<13} : {v}')

s = 0
print(f'\nEmpleado y su sueldo')
for m, c in restaurante.items():
    print(f'{m:<12}:   {c:5}')
    s=s+c
p=s/len(restaurante)

print(f'\nLa suma es {s} el promedio es {p}\n')