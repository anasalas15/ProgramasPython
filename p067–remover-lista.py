# Ejemplificar la remocion de elementos de una lista

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print('Eliminar elementos de una lista \n')

print(f'La lista {nums}, tiene {len(nums)} elementos')

print('\nRemover la primer ocurrencia de un elemento')
nums.remove(99)
print(f'La lista {nums}, tiene {len(nums)} elementos')

print('\nRemover un elemento en una posicion determinada y guardarlo, usando el metodo pop(x)')
num = nums.pop(8)
print(f'La lista {nums}, tiene {len(nums)} elementos, elemento removido {num}')

print('\nRemover el ultimo elemento de la lista y guardarlo, usando el metodo pop()')
num = nums.pop()
print(f'La lista {nums}, tiene {len(nums)} elementos, elemento removido {num}')

print('\nRemover un rango de valores en una lista, usando slice[:]')
del nums[2:5]
print(f'La lista {nums}, tiene {len(nums)} elementos')

print('\nEliminar todos los elementos de la lista, usando el metodo clear()')
nums.clear()
print(f'La lista {nums}, tiene {len(nums)} elementos')