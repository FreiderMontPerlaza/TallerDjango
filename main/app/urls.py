from django.urls import path
from .views import artista, contacto, escultura, galeria, home, manualidades, pintura

urlpatterns = [
    path('',home,name="home"),
    path('galeria/',galeria,name="galeria"),
    path('contacto/',contacto,name="contacto"),
    path('manualidades/',manualidades,name="manualidades"),
    path('escultura/',escultura,name="escultura"),
    path('pintura/', pintura, name="pintura"),
    path('artista/', artista, name="artista")

    


]
