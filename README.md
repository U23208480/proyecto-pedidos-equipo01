# Proyecto Pedidos - Equipo 01

## Integrantes
- Juan César Retuerto Ibañez - U23208480 - Módulos: clientes, productos, pedidos, integración
- Alberto Joel Ramirez Ponte - U23249035 - Módulos: documentación y pruebas

## Descripción del proyecto
Aplicación de consola para registrar y consultar pedidos de clientes de una
empresa de Servicios Turísticos Norte Azul. El proyecto nace como evaluación
práctica del uso de Git y un repositorio remoto, aplicando ramas, commits,
integración de cambios y resolución de conflictos en un flujo de trabajo
colaborativo.

## Funcionalidades principales
- **Módulo de clientes**: registrar cliente, listar clientes.
- **Módulo de productos**: registrar producto, listar productos.
- **Módulo de pedidos**: registrar pedido, consultar pedidos.

## Tecnologías utilizadas
- Python 3
- Git y GitHub (control de versiones y repositorio remoto)

## Estructura del repositorio
```
proyecto-pedidos-equipo01/
├── README.md
├── src/
│   ├── clientes/
│   ├── productos/
│   └── pedidos/
└── docs/
```

## Cómo ejecutar
```bash
python main.py
```

## Casos de uso

Esta sección describe el flujo típico de trabajo con el módulo de pedidos,
que es el que integra a los otros dos módulos del sistema.

**Orden recomendado:** como un pedido guarda únicamente el `id` del cliente
y los `id` de los productos, primero hay que registrar al cliente y a los
productos. Si se intenta registrar un pedido con ids que todavía no existen,
el pedido se crea igual pero queda apuntando a datos inexistentes.

**Caso 1 - Registrar un pedido completo**

1. En el menú principal elegir `1. Clientes` → `1. Registrar cliente` e
   ingresar nombre, documento y teléfono. El sistema devuelve el cliente
   con su `id` (por ejemplo, `id: 1`).
2. Elegir `2. Productos` → `1. Registrar producto` e ingresar nombre,
   precio y stock. Repetir por cada producto. Anotar los `id` devueltos.
3. Elegir `3. Pedidos` → `1. Registrar pedido`, escribir el `id` del
   cliente y luego los `id` de los productos separados por coma
   (por ejemplo: `1,2`).
4. El sistema confirma el pedido registrado con su propio `id`.

**Caso 2 - Consultar los pedidos**

Desde `3. Pedidos` → `2. Consultar pedidos` se listan todos los pedidos
registrados. La función `consultar_pedidos()` también acepta un
`cliente_id` opcional, de modo que puede reutilizarse para filtrar los
pedidos de un solo cliente.

**Caso 3 - Pedido inválido (validación)**

Si se intenta registrar un pedido sin cliente o sin ningún producto, la
función `registrar_pedido()` lanza un `ValueError` con el mensaje
"El pedido debe tener un cliente y al menos un producto" y el pedido **no**
se guarda. Esta validación se agregó justamente para evitar registros
vacíos en la lista.

**Consideración importante:** los datos se almacenan en memoria, por lo que
al cerrar el programa se pierde todo lo registrado. Es una limitación
conocida de esta versión y el siguiente paso natural del proyecto sería
persistir la información en una base de datos o en archivos.
