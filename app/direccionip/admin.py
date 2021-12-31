from django.contrib import admin
from ..direccionip.models import Direccionip

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DireccionipResource(resources.ModelResource):
    class Meta:
        model = Direccionip
        skip_unchanged = True
        report_skipped = True
        exclude = ('id_direccionPK',)
        import_id_fields = ('direccion','descripcion',)

class DireccionipAdmin(ImportExportModelAdmin):
    resource_class = DireccionipResource


admin.site.register(Direccionip,DireccionipAdmin)