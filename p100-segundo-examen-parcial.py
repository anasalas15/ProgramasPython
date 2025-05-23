# Se desea procesar a los emepleados de una empresa de muebles

import os;os.system('cls')

empleados = []

while True:
    print('\nCaptura de datos de los emleados, * para terminar')
    datos = {}
    nombre = input('Nombre: ')
    if nombre != '*': 
        datos['nombre'] = nombre
        datos['edad'] = int(input('Edad: '))
        datos['sexo'] = input('Sexo (h/m): ').lower()
        datos['sueldo'] = float(input('Sueldo: '))
        datos['pasatiempos'] = input("Pasatiempos (separados por coma): ").split(',')
        empleados.append(datos)
    else: break

#Imprimir los datos como se guardan en la lista 
print(f'\nDatos de empleados {empleados} - {len(empleados)}')

#Imprimir Tabla de datos
print('\nTabla de datos: ')

print('-'*80)
for llave in empleados[0].keys():
    print(f'{llave:<12}', end='')
print()
print('-'*80)

for empleado in empleados:
    for clave, valor in empleado.items():
        if clave == 'pasatiempos':
            valor = ", ".join(valor)
        print(f'{str(valor):<12}', end='') 
    
    print()
print('-' * 80)

#Imprimir Resumen
print('\nResumen: ')

hombres = 0
mujeres = 0
suma_edades = 0
suma_sueldos = 0
pasatiempos_contados = {}

mayor = empleados[0]
menor = empleados[0]

for emp in empleados:
    if emp['sexo'] == 'h':
        hombres += 1
    elif emp['sexo'] == 'm':
        mujeres += 1

    suma_edades += emp['edad']
    suma_sueldos += emp['sueldo']

    if emp['edad'] > mayor['edad']:
        mayor = emp
    if emp['edad'] < menor['edad']:
        menor = emp

    for p in emp['pasatiempos']:
        p = p.strip()
        if p in pasatiempos_contados:
            pasatiempos_contados[p] += 1
        else:
            pasatiempos_contados[p] = 1

print(f'Empleados : {len(empleados)}')
print(f'Mujeres   : {mujeres}')
print(f'Hombres   : {hombres}')

print('Pasatiempos:', end=' ')
for p, c in pasatiempos_contados.items():
    print(f'{p}/{c}', end=', ')
print()

promedio_edad = suma_edades / len(empleados)
promedio_sueldo = suma_sueldos / len(empleados)

print(f'Edad -> suma: {suma_edades}, promedio: {promedio_edad:.1f}')
print(f'Sueldo -> suma: {suma_sueldos:,.2f}, promedio: {promedio_sueldo:,.2f}')
print(f'{mayor["nombre"]} de {mayor["edad"]} es el mayor, {menor["nombre"]} de {menor["edad"]} es el menor.')