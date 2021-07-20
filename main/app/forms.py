from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from .models import  Producto
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


        widgets = {
            "fecha_creada": forms.SelectDateWidget()
        }



class CustomUserCreationForm(UserCreationForm):
    pass