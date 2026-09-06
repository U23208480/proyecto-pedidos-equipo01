"""Módulo de pedidos: registrar y consultar pedidos."""

pedidos = []


def registrar_pedido(cliente_id, productos_ids):
    if cliente_id is None or not productos_ids:
        raise ValueError("El pedido debe tener un cliente y al menos un producto")
    pedido = {
        "id": len(pedidos) + 1,
        "cliente_id": cliente_id,
        "productos_ids": productos_ids,
    }
    pedidos.append(pedido)
    return pedido


def consultar_pedidos(cliente_id=None):
    if cliente_id is None:
        return pedidos
    return [p for p in pedidos if p["cliente_id"] == cliente_id]
