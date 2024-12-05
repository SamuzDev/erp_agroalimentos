from django.contrib import admin
from .models import Proveedor, Producto, OrdenCompra, Inventario, SolicitudPedido

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(OrdenCompra)
admin.site.register(SolicitudPedido)
admin.site.register(Inventario)