from django.contrib import admin
from catalog.models import Deudor, Deuda


class DeudorAdmin(admin.ModelAdmin):
    list_display = ('rut','nombres','apellido_p','apellido_m','estado_civil','created_at','updated_at')

class DeudaAdmin(admin.ModelAdmin):
    list_display = ('acreedor','date','monto_deuda','created_at','updated_at')    

admin.site.register(Deudor, DeudorAdmin)
admin.site.register(Deuda, DeudaAdmin)