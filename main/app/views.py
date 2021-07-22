from django import contrib
from django import http
from django.contrib.auth.forms import UsernameField
from django.core import paginator
from django.http import request
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render,redirect,get_list_or_404
from .forms import ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login


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

def equipo(request):
    return render(request,'app/equipo.html')

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
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,5)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
    'entity':productos,
    'paginator': paginator
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
            messages.success(request,"Producto modificado exitosamente")
            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request,'app/producto/modificar.html',data)




def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request,"Producto eliminado de la lista")
    return redirect(to="listar_producto")


def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(Username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Usuario registrado exitosamente")
            return redirect(to="home")
        data['form'] = formulario
    return render(request,'registration/registro.html',data)


def artista1(request):
    return render(request,'app/artista1.html')