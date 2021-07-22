from django.http import request
from django.urls import path
from .views import artista, artista1, equipo,escultura, galeria, home, manualidades, modificar_producto, pintura,agregar_producto,listar_producto,eliminar_producto,registro

urlpatterns = [
    path('',home,name="home"),
    path('galeria/',galeria,name="galeria"),
    path('manualidades/',manualidades,name="manualidades"),
    path('escultura/',escultura,name="escultura"),
    path('pintura/', pintura, name="pintura"),
    path('equipo/',equipo, name="equipo"),
    path('artista/', artista, name="artista"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/',listar_producto, name="listar_producto"),
    path('modificar-producto/<id>/',modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/',registro,name="registro"),
    path('artista1/',artista1,name="artista1")




    

    


]
