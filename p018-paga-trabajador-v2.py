# Calcular la paga de un trabajador cnsiderando qye las horas extras se pagan al doble 

print('# Calcular la paga de un trabajador cnsiderando qye las horas extras se pagan al doble')

nombre = input('Nombre del trabajador: ')
horas  = int(input('Horas trabajadas: '))
paga   = float(input('Paga x Hora: '))

extra = pextra = total = 0 # asignamos el valor de 0 a las 3 variables 

if horas > 40: 
    extra = horas - 40
    pextra = extra * ( 2 * paga )
    total = ( 40 * paga ) + pextra
else:
    total = paga * horas

print(f'{nombre} trabajo {horas} horas, con una paga de {paga} pesos,paga extra {pextra} pesos, pago total {total}')

