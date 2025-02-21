# Convierte un numero entero del 1 al 10 en numero romano

print('Convierte un numero entero del 1 al 10 en numero romano')

num = int(input('Dame un numero entero positivo entre el 1 y 10: '))

if num == 1:
    print('1, I')
elif num == 2:
    print('2, II')
elif num == 3:
    print('3, III')
elif num == 4:
    print('4, IV')
elif num == 5:
    print('5, V')
elif num == 6:
    print('6, VI')
elif num == 7:
    print('7, VII')
elif num == 8:
    print('8, VIII')
elif num == 9:
    print('9, IX')
elif num == 10:
    print('10, X')
elif num > 10:
    print(f'{num}, invalido')
