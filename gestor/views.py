from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FormularioRegistroUsuario, FormularioLogin
from .models import Cliente



def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistroUsuario(request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            correo = formulario.cleaned_data.get('email')
            contraseña = formulario.cleaned_data.get('password1')
            usuario, cliente = Cliente.crear_usuario(nombre_usuario, correo, contraseña)
            login(request, usuario)
            messages.success(request, f'¡Cuenta creada para {nombre_usuario}! Has iniciado sesión.')
            return redirect('inicio')  # Asegúrate de tener una vista 'inicio'
        else:
            for field, errors in formulario.errors.items():
                for error in errors:
                    messages.error(request, f'{formulario.fields[field].label}: {error}')
    else:
        formulario = FormularioRegistroUsuario()
    return render(request, 'registro.html', {'formulario': formulario})


def inicio_sesion(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['username']
            contraseña = formulario.cleaned_data['password']
            usuario = authenticate(request, username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, f'¡Bienvenido, {nombre_usuario}!')
                return redirect('inicio')  # Redirigir a la página de inicio después del login
            else:
                messages.error(request, 'Nombre de usuario o contraseña inválidos')
    else:
        formulario = FormularioLogin()
    return render(request, 'login.html', {'formulario': formulario})

@login_required
def inicio(request):
    return render(request, 'inicio.html')