"""Punto de entrada de la aplicación de pedidos (menú interactivo de consola)."""

from src.clientes.clientes import registrar_cliente, listar_clientes
from src.productos.productos import registrar_producto, listar_productos
from src.pedidos.pedidos import registrar_pedido, consultar_pedidos


def menu_clientes():
    print("\n1. Registrar cliente\n2. Listar clientes\n0. Volver")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        nombre = input("Nombre: ").strip()
        documento = input("Documento: ").strip()
        telefono = input("Teléfono: ").strip()
        cliente = registrar_cliente(nombre, documento, telefono)
        print("Cliente registrado:", cliente)
    elif opcion == "2":
        for c in listar_clientes():
            print(c)


def menu_productos():
    print("\n1. Registrar producto\n2. Listar productos\n0. Volver")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        nombre = input("Nombre: ").strip()
        precio = float(input("Precio: ").strip())
        stock = int(input("Stock: ").strip())
        producto = registrar_producto(nombre, precio, stock)
        print("Producto registrado:", producto)
    elif opcion == "2":
        for p in listar_productos():
            print(p)


def menu_pedidos():
    print("\n1. Registrar pedido\n2. Consultar pedidos\n0. Volver")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        cliente_id = int(input("ID del cliente: ").strip())
        ids_texto = input("IDs de productos separados por coma: ").strip()
        productos_ids = [int(i) for i in ids_texto.split(",") if i.strip()]
        pedido = registrar_pedido(cliente_id, productos_ids)
        print("Pedido registrado:", pedido)
    elif opcion == "2":
        for p in consultar_pedidos():
            print(p)


def menu_principal():
    while True:
        print("\n=== Sistema de Pedidos ===")
        print("1. Clientes")
        print("2. Productos")
        print("3. Pedidos")
        print("0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_pedidos()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu_principal()
