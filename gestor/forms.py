from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rol, Cliente , Tecnico , TicketAsignado ,Ticket 

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nom_rol']

class ClienteForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo_electronico', 'telefono', 'contraseña']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.contraseña = make_password(self.cleaned_data['contraseña'])
        if commit:
            instance.save()
        return instance

class TecnicoForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    
    class Meta:
        model = Tecnico
        fields = ['nombre', 'correo_electronico', 'telefono', 'contraseña', 'id_rol']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.contraseña = make_password(self.cleaned_data['contraseña'])
        if commit:
            instance.save()
        return instance

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['descripcion', 'estado']

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
