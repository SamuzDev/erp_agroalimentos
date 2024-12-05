from gestion.models import Proveedor, Categoria, Producto, SolicitudPedido, OrdenCompra, Inventario

def cargar_datos():
    # Crear proveedores
    proveedor_1 = Proveedor.objects.create(
        nombre='Proveedor A',
        direccion='Calle Falsa 123, Ciudad',
        telefono='123456789',
        email='proveedorA@agro.com'
    )

    proveedor_2 = Proveedor.objects.create(
        nombre='Proveedor B',
        direccion='Avenida Siempre Viva 456, Ciudad',
        telefono='987654321',
        email='proveedorB@agro.com'
    )

    # Crear categorías solo si no existen
    categoria_1, created = Categoria.objects.get_or_create(nombre='Galletas')
    categoria_2, created = Categoria.objects.get_or_create(nombre='Azúcar Refinada')
    categoria_3, created = Categoria.objects.get_or_create(nombre='Azúcar Morena')
    categoria_4, created = Categoria.objects.get_or_create(nombre='Alimento para Pollos')

    # Crear productos
    producto_1 = Producto.objects.create(
        nombre='Galletas de vainilla',
        categoria=categoria_1,
        precio=1.50,
        stock=100,
        proveedor=proveedor_1
    )

    producto_2 = Producto.objects.create(
        nombre='Azúcar Refinada',
        categoria=categoria_2,
        precio=0.75,
        stock=200,
        proveedor=proveedor_2
    )

    # Crear solicitudes de pedido
    solicitud_pedido_1 = SolicitudPedido.objects.create(
        numero_solicitud='SOL001',
        producto=producto_1,
        cantidad=500,
        solicitante='Cliente A',  # Suponiendo que ya existe o se puede crear un cliente
        estado='pendiente'
    )

    solicitud_pedido_2 = SolicitudPedido.objects.create(
        numero_solicitud='SOL002',
        producto=producto_2,
        cantidad=300,
        solicitante='Cliente B',  # Suponiendo que ya existe o se puede crear un cliente
        estado='pendiente'
    )

    # Crear órdenes de compra
    orden_compra_1 = OrdenCompra.objects.create(
        numero_orden='ORD001',
        proveedor=proveedor_1,
        fecha_orden='2024-12-05',
        total=5000.00,
        solicitud_pedido=solicitud_pedido_1
    )

    orden_compra_2 = OrdenCompra.objects.create(
        numero_orden='ORD002',
        proveedor=proveedor_2,
        fecha_orden='2024-12-06',
        total=3000.00,
        solicitud_pedido=solicitud_pedido_2
    )

    # Crear inventarios
    inventario_1 = Inventario.objects.create(
        producto=producto_1,
        cantidad=1000,
        orden_compra=orden_compra_1,
        tipo_inventario='terminados'
    )

    inventario_2 = Inventario.objects.create(
        producto=producto_2,
        cantidad=1500,
        orden_compra=orden_compra_2,
        tipo_inventario='materia_prima'
    )

    print("Datos cargados exitosamente.")

if __name__ == "__main__":
    cargar_datos()
