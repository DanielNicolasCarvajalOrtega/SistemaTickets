from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Rol, Ticket, TicketAsignado

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nom_rol']
        labels = {
            'nom_rol': 'Nombre del Rol',
        }

class UsuarioForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput())
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['nombre', 'correo_electronico', 'telefono', 'id_rol', 'es_tecnico']
        labels = {
            'nombre': 'Nombre',
            'correo_electronico': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'id_rol': 'Rol',
            'es_tecnico': '¿Es técnico?',
        }
        widgets = {
            'es_tecnico': forms.CheckboxInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get("contraseña")
        confirmar_contraseña = cleaned_data.get("confirmar_contraseña")

        if contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data

class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField(required=True)
    es_tecnico = forms.BooleanField(required=False, initial=False, label='¿Es técnico?')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'es_tecnico')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['descripcion', 'estado', 'id_usuario']
        labels = {
            'descripcion': 'Descripción',
            'estado': 'Estado',
            'id_usuario': 'Usuario',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'estado': forms.Select(choices=Ticket.ESTADO_OPCIONES),
        }

class TicketAsignadoForm(forms.ModelForm):
    class Meta:
        model = TicketAsignado
        fields = ['id_ticket', 'id_tecnico']
        labels = {
            'id_ticket': 'Ticket',
            'id_tecnico': 'Técnico Asignado',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_tecnico'].queryset = Usuario.objects.filter(es_tecnico=True)

class FormularioLogin(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)