# Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente

print('Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente')

numero = int(input('Dame un numero entero positivo entre el 1 y el 7: '))

if numero == 1:
    print('1, Lunes')
elif numero == 2:
    print('2, Martes')
elif numero == 3:
    print('3, Miercoles')
elif numero == 4:
    print('4, Jueves')
elif numero == 5:
    print('5, Viernes')
elif numero == 6:
    print('6, Sabado')
elif numero == 7:
    print('7, Domingo')
elif numero > 7:
    print(f'{numero}, invalido')
