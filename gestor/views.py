from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClienteForm, TecnicoForm, FormularioRegistroUsuario, FormularioLogin
from .models import Cliente, Tecnico


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
            return redirect('inicio')
        else:
            for field, errors in formulario.errors.items():
                for error in errors:
                    messages.error(request, f'{formulario.fields[field].label}: {error}')
    else:
        formulario = FormularioRegistroUsuario()
    return render(request, 'registro.html', {'formulario': formulario})


def crear_cliente(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('inicio')
    else:
        formulario = ClienteForm()
    return render(request, 'crear_cliente.html', {'formulario': formulario})


def crear_tecnico(request):
    if request.method == 'POST':
        formulario = TecnicoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Técnico creado exitosamente.')
            return redirect('inicio')
    else:
        formulario = TecnicoForm()
    return render(request, 'crear_tecnico.html', {'formulario': formulario})


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
                return redirect('inicio')
            else:
                messages.error(request, 'Nombre de usuario o contraseña inválidos')
    else:
        formulario = FormularioLogin()
    return render(request, 'login.html', {'formulario': formulario})


@login_required
def inicio(request):
    return render(request, 'inicio.html')
