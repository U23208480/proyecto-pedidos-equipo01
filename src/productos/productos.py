"""Módulo de productos: registrar y listar productos.

Funciona igual que el módulo de clientes: los productos se mantienen en la
lista `productos` en memoria y cada uno recibe un `id` correlativo
generado automáticamente.

El `id` que devuelve `registrar_producto` es el que luego se usa en el
módulo de pedidos para indicar qué productos incluye cada pedido.
"""

productos = []


# Registra un producto nuevo con su nombre, precio y stock inicial.
# El id se asigna solo, siguiendo el correlativo de la lista.
# Devuelve el diccionario creado para confirmarlo en pantalla.
def registrar_producto(nombre, precio, stock):
    producto = {
        "id": len(productos) + 1,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }
    productos.append(producto)
    return producto


# Devuelve todos los productos registrados hasta el momento.
# Sirve para consultar los ids disponibles antes de armar un pedido.
def listar_productos():
    return productos
