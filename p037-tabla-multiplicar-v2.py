# Imprime las tablas de 1 a n, hasta 10 

while(True):
    n = int(input('Hasta que tabla quieres ? '))
    m = int(input('Hasta donde             ? '))

    t = 1
    while t <= n :
        print(f'\nTabla {n}\n')

        c = 1 
        while c <= m : 
            print(f'{t} x {c} = {t * c}')
            c += 1

        t += 1

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')

