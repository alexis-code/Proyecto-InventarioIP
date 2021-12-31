from django.contrib import admin
from ..activo.models import Activo

admin.site.register(Activo)

admin.site.site_title="Inventario de Redes y Activos"
admin.site.site_header = "Inventario de Redes y Activos"
admin.site.site_url = "/activo/index"
