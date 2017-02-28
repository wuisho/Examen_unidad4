from django.contrib import admin
from .models import Libros
# Register your models here.

class LibrosAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "Nombre", "Autor", "Editorial", "ISBN", "Precio"]
    search_fields = ["Precio"]
    list_editable = ["Nombre"]
    list_filter = ["Autor"]
    class Meta:
        model = Libros

admin.site.register(Libros,LibrosAdmin)
