"""Módulo de pedidos: registrar y consultar pedidos.

Es el módulo que une a los otros dos: un pedido guarda el `id` del cliente
y la lista de `id` de los productos solicitados, no los datos completos.
Por eso conviene registrar primero el cliente y los productos.

Incluye una validación para evitar pedidos vacíos o sin cliente, que fue
el error corregido en el commit `fix: corregir validación de pedidos sin
cliente o productos`.
"""

pedidos = []


# Registra un pedido asociando un cliente con uno o más productos.
# Antes de crear el pedido se valida que exista un cliente y al menos un
# producto; si no se cumple, se lanza ValueError y el pedido no se guarda.
# Esto evita que queden registros vacíos o inválidos en la lista.
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


# Consulta los pedidos registrados.
# Si no se envía cliente_id, devuelve todos los pedidos.
# Si se envía, filtra y devuelve solo los pedidos de ese cliente.
def consultar_pedidos(cliente_id=None):
    if cliente_id is None:
        return pedidos
    return [p for p in pedidos if p["cliente_id"] == cliente_id]
