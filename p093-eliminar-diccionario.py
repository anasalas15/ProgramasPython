# Cree un diccionario de llave de cadena municipios
# Eliminar elementos del diccionario

municipios = {
    'Apozol' : 1863, 
    'Calera' : 1868, 
    'Fresnillo' : 1554, 
    'Guadalupe' : 1821, 
    'Jalpa' : 1824, 
    'Jerez' : 1824, 
    'Loreto' : 1931,
    'Mazapil' : 1824, 
    'Momax' : 1857
}

print(f'Diccionario de municipios: {municipios} - {len(municipios)}\n')

#Eliminar la llave Apozol usando del
del municipios['Apozol']

# Eliminar la llave Fresnillo usando pop()
municipios.pop('Fresnillo')

# Eliminar la ultima llave usando popitem()
municipios.popitem()

for k, v in municipios.items():
    print(f'{k:<13} : {v}')

municipios.clear()
print(f'\nDiccionario de municipios: {municipios} - {len(municipios)}')