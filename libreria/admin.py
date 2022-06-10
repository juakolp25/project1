from django.contrib import admin
from .models import Tatuaje, Diseno, Contacto

# Register your models here.

class TatuajeAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha_fabricacion", "descripcion", "imagen"]
    search_fields = ["nombre"]

class DisenoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha_fabricacion", "descripcion", "imagen"]
    search_fields = ["nombre"]

admin.site.register(Tatuaje, TatuajeAdmin)
admin.site.register(Diseno, DisenoAdmin)
admin.site.register(Contacto)