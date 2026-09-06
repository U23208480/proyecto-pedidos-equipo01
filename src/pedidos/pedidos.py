"""Módulo de pedidos: registrar y consultar pedidos."""

pedidos = []


def registrar_pedido(cliente_id, productos_ids):
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
