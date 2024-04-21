from django.contrib import admin
from .models import Casillero, Arrendatario, Contrato

class ContratoAdmin(admin.ModelAdmin):
    list_display = ('casillero', 'arrendatario', 'fecha_inicio', 'fecha_fin', 'pagado')
    list_filter = ('pagado', 'fecha_inicio', 'fecha_fin')
    search_fields = ('arrendatario__nombre', 'casillero__numero')

admin.site.register(Casillero)
admin.site.register(Arrendatario)
admin.site.register(Contrato)