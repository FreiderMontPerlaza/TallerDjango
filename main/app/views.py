from django.http import request
from django.shortcuts import get_object_or_404, render,redirect,get_list_or_404
from .forms import ProductoForm

from .models import Producto

# Create your views here.
def home(request):
    return render(request,'app/home.html')


def galeria(request):
     productos = Producto.objects.all()
     data = {
         'productos':productos
     }
     return render(request,'app/galeria.html',data)




def manualidades(request):
    return render(request,'app/manualidades.html')


def escultura(request):
    return render(request,'app/escultura.html') 

def pintura(request):
    return render(request,'app/pintura.html')

def artista(request):
    return render(request,'app/artista.html')
  


def agregar_producto(request):
    data = {
        'form': ProductoForm()

    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request,'app/producto/agregar.html',data)




def listar_producto(request):
    productos = Producto.objects.all()

    data = {
    'productos':productos
    }
    return render(request,'app/producto/listar.html',data)


def modificar_producto(request,id):

    producto = get_object_or_404(Producto,id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }


    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request,'app/producto/modificar.html',data)






def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    return redirect(to="listar_producto")

