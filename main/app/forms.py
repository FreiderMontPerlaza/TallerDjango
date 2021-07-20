from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from .models import  Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


        widgets = {
            "fecha_creada": forms.SelectDateWidget()
        }



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]