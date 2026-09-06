"""Punto de entrada de la aplicación de pedidos (demo de consola)."""

from src.clientes.clientes import registrar_cliente, listar_clientes
from src.productos.productos import registrar_producto, listar_productos
from src.pedidos.pedidos import registrar_pedido, consultar_pedidos


def demo():
    cliente = registrar_cliente("Ana Torres", "12345678", "999111222")
    producto = registrar_producto("Teclado mecánico", 120.0, 10)
    registrar_pedido(cliente["id"], [producto["id"]])

    print("Clientes:", listar_clientes())
    print("Productos:", listar_productos())
    print("Pedidos:", consultar_pedidos())


if __name__ == "__main__":
    demo()
