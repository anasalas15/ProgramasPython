#Primer examen parcial
#Ana Teresa Rosales Salas
# Se lleva el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo de usuario, paquete y cantidad.

print('Universidad Patito SA de CV')
print('Sistema de Inscripción Congreso de Sistemas\n')

total = 0  

while True:
    usuario = int(input('Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500 ? '))

    if  usuario == 1:
        preciou = 100
        nombreu = 'Alumno'
    elif usuario == 2:
        preciou = 200
        nombreu = 'Trabajador'
    elif usuario == 3:
        preciou = 500
        nombreu = 'Docente'
    else:
        print('Opción no válida')
        continue

    paquete = int(input('Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900 ? '))

    if paquete == 1:
        preciop = 600
        nombrep = 'Solo conferencias'
    elif paquete == 2:
        preciop = 800
        nombrep = 'Con eventos sociales'
    elif paquete == 3:
        preciop = 900
        nombrep = 'Con kit de acceso'
    else:
        print('Opción no válida')
        continue
 
    cantidad = int(input('Cantidad ? '))

    subtotal = ( preciou + preciop ) * cantidad

    descuento = 0
    porcentaje_descuento = 0

    if subtotal > 5000:
        if usuario == 1:
            porcentaje_descuento = 20
        elif usuario == 2:
            porcentaje_descuento = 10
        elif usuario == 3:
            porcentaje_descuento = 5

        descuento = (subtotal * porcentaje_descuento) / 100

    totalventa = subtotal - descuento
    total += totalventa

    print(f'Tu pedido fue: {cantidad}, Tipo de usuario: {nombreu}, Tipo de paquete: {nombrep}')
    print(f'Subtotal: {subtotal} con un descuento de: {descuento:.1f} ({porcentaje_descuento:.1f}%) y un total de {totalventa:.1f}\n')

    
    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print(f'\nImporte Total de la Venta: {total:.2f}')
print('Proceso Terminado ')