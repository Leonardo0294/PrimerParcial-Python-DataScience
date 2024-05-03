import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

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

# DataFrame de la lista de los productos 
df_productos = pd.DataFrame(productos)

# Valor total del inventario para cada producto
df_productos['valor_total'] = df_productos['precio'] * df_productos['cantidad_disponible']

#Valor total del inventario para cada producto
print("Valor total del inventario:")
print(df_productos[['nombre', 'valor_total']])

# Valor total del inventario sumando los valores totales de cada producto
valor_total_inventario = df_productos['valor_total'].sum()
print("\nValor total del inventario (suma de todos los productos):", valor_total_inventario)

#Aqui se simulan algunas ventas 
ventas = [
    {"nombre": "Gorra", "cantidad_vendida": 10},
    {"nombre": "Vestido", "cantidad_vendida": 5},
    {"nombre": "Pantalón", "cantidad_vendida": 15},
    {"nombre": "Bolsa", "cantidad_vendida": 8},
    {"nombre": "Cinturon", "cantidad_vendida": 50},
    {"nombre": "Vestido", "cantidad_vendida": 30},
    {"nombre": "Corbata", "cantidad_vendida": 60},
    {"nombre": "Collar", "cantidad_vendida": 50},
]

for venta in ventas:
    producto = venta['nombre']
    cantidad_vendida = venta['cantidad_vendida']
# Se actualiza la cantidad de productos después de la venta
    df_productos.loc[df_productos['nombre'] == producto, 'cantidad_disponible'] -= cantidad_vendida

df_cantidad_disponible = df_productos[['nombre', 'cantidad_disponible']]

lista_productos = df_cantidad_disponible['nombre', 'cantidad_disponible'].value_counts().sort_index()

#Se crea un grafico de barras
plt.figure(figsize=(10, 6))
plt.plot(cantidad_productos.index, cantidad_productos.values, marker='o', linestyle='-', color='b')
    
#Grafico config
plt.title('Lista de productos')
plt.xlabel('Nombre de productos')
plt.ylabel('Cantidad disponible de cada producto')
plt.grid(True)
    

plt.show()

productos()
