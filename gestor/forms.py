from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rol, Cliente, Tecnico, Ticket, TicketAsignado

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nom_rol']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo_electronico', 'telefono']

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'correo_electronico', 'telefono']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['descripcion', 'estado', 'id_cliente']

class TicketAsignadoForm(forms.ModelForm):
    class Meta:
        model = TicketAsignado
        fields = ['id_ticket', 'id_tecnico']

class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

class FormularioLogin(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

