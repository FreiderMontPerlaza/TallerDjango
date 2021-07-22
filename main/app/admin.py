from django.contrib import admin
from.models import Marca,Producto
from .forms import ProductoForm

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","disponible","marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca","disponible"]
    list_per_page = 5
    form = ProductoForm

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)

