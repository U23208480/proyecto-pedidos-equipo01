"""Módulo de productos: registrar y listar productos."""

productos = []


def registrar_producto(nombre, precio, stock):
    producto = {
        "id": len(productos) + 1,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }
    productos.append(producto)
    return producto


def listar_productos():
    return productos
