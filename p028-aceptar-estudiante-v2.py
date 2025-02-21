# Aceptar estudiantes en base a ciertos criterios v2

print('Universidad Kitty Kat SA')

nombre = input('dame tu nombre > ')
sexo = input('Dame tu sexo (H/M) >  ')
edad = int(input('dame tu edad > '))


if sexo != 'M':
    print(f'{nombre}, {edad}, {sexo} solo aceptamos mujeres')
elif edad <= 21:
    print(f'{nombre}, eres mujer, pero no tienes la edad, solo aceptamos mayores de 21')
else:
    print ('Dame 3 calificaciones separadas por <Enter> ')
    c1, c2, c3 = float(input()), float(input()), float(input())
    promedio = ( c1 + c2 + c3 ) / 3 

    if promedio < 8 or promedio > 9.5:
        print(f'{nombre}, eres mujer, tienes la edad, pero solo permitimos promedios entre 8 a 9.5 ')
    else: 
        print(f'{nombre}, has sido aceptada, tu edad de {edad} y tus calificaciones de {c1}, {c2}, {c3} lo permiten')

