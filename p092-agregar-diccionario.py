# Crear un diccionario de llave de cadena, ventas
# Agregar elementos al diccionario

import os; os.system('cls')

ventas = {
    'Juan'  : 1550,
    'Jose'  : 2600,
    'Maria' : 2220
}

#Mostrar diccionario
print(f'Diccionario de ventas: {ventas} - {len(ventas)}')

#Agregar elementos con []
ventas ['Rocio'] = 2500
ventas ['Mateo'] = 1567

#Agregar elementos con update()
ventas.update({'Andrea': 9567})
ventas.update({'Miguel': 1234})

print('\nDiccionario actualizado')
print(f'Elemntos en el diccionario: {len(ventas)}\n')
for k, v in ventas.items():
    print(f'{k:<10} : {v}')
