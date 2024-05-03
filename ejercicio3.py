import pandas as pd 

productos = [
    {"nombre": "Camiseta", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
    {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
    {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
    {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
    {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
    {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
    {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
    {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
    {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible": 25},
    {"nombre": "Calcetines", "precio": 10, "cantidad_disponible": 150},
    {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
    {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
    {"nombre": "Pendientes", "precio": 15, "cantidad_disponible": 180},
    {"nombre": "Cinturón", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
    {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
    {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
    {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
    {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]

# Se crea una DatFrame a traves de una lista de productos
df_productos = pd.DataFrame(productos)

# Calcular el valor total del inventario para cada producto
df_productos['valor_total'] = df_productos['precio'] * df_productos['cantidad_disponible']

# Mostrar el valor total del inventario para cada producto
print("Valor total del inventario por producto:")
print(df_productos[['nombre', 'valor_total']])

# Calcular el valor total del inventario sumando los valores totales de cada producto
valor_total_inventario = df_productos['valor_total'].sum()
print("\nValor total del inventario (suma de todos los productos):", valor_total_inventario)

# Simular algunas ventas y actualizar la cantidad disponible de productos vendidos
ventas = [
    {"nombre": "Gorra", "cantidad_vendida": 10},
    {"nombre": "Vestido", "cantidad_vendida": 5},
    {"nombre": "Pantalón", "cantidad_vendida": 20},
]

for venta in ventas:
    producto = venta['nombre']
    cantidad_vendida = venta['cantidad_vendida']
    # Actualizar la cantidad disponible después de la venta
    df_productos.loc[df_productos['nombre'] == producto, 'cantidad_disponible'] -= cantidad_vendida

# Semuestra la cantidad restante disponible luego de cada venta 
print("\nCantidad restante disponible de cada producto después de las ventas:")
print(df_productos[['nombre', 'cantidad_disponible']])

# Se crea un dataFrame que muestra la cantidad disponible de productos 
df_cantidad_disponible = df_productos[['nombre', 'cantidad_disponible']]
print("\nDataFrame con nombres de productos y cantidad disponible:")
print(df_cantidad_disponible)