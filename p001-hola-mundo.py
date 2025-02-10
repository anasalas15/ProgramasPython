# Leer y mostrar datos

print('Leyendo datos del usuario, luego enviar un saludito :D')

nombre = input('Dame tu nombre: ')
edad   = input('Dame tu edad: ')
peso   = float(input('Dame tu peso: ')) #float convierte la cadena introducida a flotante

print(f'{nombre} bienvenido al lenguaje Python. Tu edad es {edad} y tu peso es {peso}')
print('\n')
print(type(nombre))
print(type(edad))
print(type(peso))