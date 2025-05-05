# Procesa el pedido de una pizza con diferentes ingredientes

import os; os.system('cls')

# Diccionario de precios por ingrediente
ingredientes = {
    'T': 1.5,
    'P': 3.5,
    'C': 3.74,
    'A': 0.40
}

base = 15
subtotal_ingredientes = 0
descuento = 0

# Solicitar pedido al usuario
pedido = input('Ingredientes (T)omate, (P)eperoni, (C)hampinones, (A)guacate ? ').upper()

# Calcular subtotal de ingredientes
for ingrediente in pedido:
    if ingrediente in ingredientes:
        subtotal_ingredientes += ingredientes[ingrediente]

# Calcular subtotal general (base + ingredientes)
subtotal = base + subtotal_ingredientes
total = subtotal

# Aplicar descuento si corresponde
if subtotal >= 20:
    descuento = subtotal * 0.05
    total = subtotal - descuento

# Mostrar resumen
print(f'\nLos ingredientes que elegiste fueron: {pedido}')
print(f'Subtotal sin descuento: ${subtotal:.2f}')
print(f'El importe del descuento es: ${descuento:.2f}')
print(f'\nTotal a pagar: ${total:.2f}')

