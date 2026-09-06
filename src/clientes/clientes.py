"""Módulo de clientes: registrar y listar clientes."""

clientes = []


def registrar_cliente(nombre, documento, telefono):
    cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre,
        "documento": documento,
        "telefono": telefono,
    }
    clientes.append(cliente)
    return cliente


def listar_clientes():
    return clientes
