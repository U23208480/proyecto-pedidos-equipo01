"""Módulo de clientes: registrar y listar clientes.

Los clientes se guardan en memoria, dentro de la lista `clientes`. Cada
cliente es un diccionario y su `id` se genera de forma automática y
correlativa, por lo que no hace falta enviarlo al registrar.

Nota: al ser almacenamiento en memoria, los datos se pierden al cerrar el
programa. Para que persistan habría que conectar una base de datos o
guardar en un archivo.
"""

clientes = []


# Crea un cliente nuevo con los datos recibidos y lo agrega a la lista.
# El id se calcula como la cantidad actual de clientes + 1, así el primero
# registrado queda con id 1, el segundo con id 2, y así sucesivamente.
# Devuelve el diccionario creado para poder mostrarlo en el menú.
def registrar_cliente(nombre, documento, telefono):
    cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre,
        "documento": documento,
        "telefono": telefono,
    }
    clientes.append(cliente)
    return cliente


# Devuelve la lista completa de clientes registrados hasta el momento.
# Se usa desde el menú de consola para recorrerlos e imprimirlos.
def listar_clientes():
    return clientes
