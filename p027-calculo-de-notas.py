# Calculo de promedio de 5 calificaciones, se evalua el resultado e imprime un msj de acuerdo al promedio obtenido  

print('Calculo de promedio de 5 calificaciones, se evalua el resultado e imprime un msj de acuerdo al promedio obtenido')

print('Dame 5 calificaciones separadas por espacio: ')

n1, n2, n3, n4, n5 = input().split()
n1, n2, n3, n4, n5 = [float(n1), float(n2), float(n3), float(n4), float(n5) ]
prom = ( n1 + n2 + n3 + n4 + n5 ) / 5

if 0 < prom < 6:
    print('Quedas reprobado')
elif 6 < prom < 7:
    print('Pasas de panzaso')
elif 7 < prom < 8:
    print('Muy bien, puedes mejorar')
elif 8 < prom < 9:
    print('Excelente sigue asi')
elif 9 < prom <= 10:
    print('Perfecto tu esfuerzo valio la pena')


