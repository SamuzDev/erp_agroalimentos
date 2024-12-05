from django.db import models

# Modelo para las categorías de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para los proveedores
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Modelo para los productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo para solicitudes de pedido (SOLPED)
class SolicitudPedido(models.Model):
    ESTADOS_SOLPED = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    numero_solicitud = models.CharField(max_length=20, unique=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    solicitante = models.CharField(max_length=100)
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS_SOLPED, default='pendiente')
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"SOLPED {self.numero_solicitud} - {self.producto.nombre}"

# Modelo para órdenes de compra
class OrdenCompra(models.Model):
    numero_orden = models.CharField(max_length=20, unique=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_orden = models.DateField()
    total = models.DecimalField(max_digits=15, decimal_places=2)
    solicitud_pedido = models.ForeignKey(SolicitudPedido, on_delete=models.CASCADE, related_name='ordenes_compra')

    def __str__(self):
        return f"Orden {self.numero_orden} - {self.proveedor.nombre}"

# Modelo para inventarios (genérico)
class Inventario(models.Model):
    TIPOS_INVENTARIO = [
        ('terminados', 'Productos Terminados'),
        ('materia_prima', 'Materia Prima o Insumos')
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_actualizacion = models.DateField(auto_now=True)
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, related_name='inventarios')
    tipo_inventario = models.CharField(max_length=20, choices=TIPOS_INVENTARIO, default='materia_prima')

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} ({self.get_tipo_inventario_display()})"
