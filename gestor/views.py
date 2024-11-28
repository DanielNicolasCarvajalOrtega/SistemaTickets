from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UsuarioForm, FormularioRegistroUsuario, FormularioLogin
from .models import Usuario

def es_admin(user):
    return user.is_superuser

def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistroUsuario(request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            correo = formulario.cleaned_data.get('email')
            contraseña = formulario.cleaned_data.get('password1')
            es_tecnico = formulario.cleaned_data.get('es_tecnico', False)
            usuario_auth, usuario = Usuario.crear_usuario(nombre_usuario, correo, contraseña, es_tecnico)
            login(request, usuario_auth)
            messages.success(request, f'¡Cuenta creada para {nombre_usuario}! Has iniciado sesión.')
            return redirect('inicio_cliente' if not es_tecnico else 'inicio_tecnico')
        else:
            for field, errors in formulario.errors.items():
                for error in errors:
                    messages.error(request, f'{formulario.fields[field].label}: {error}')
    else:
        formulario = FormularioRegistroUsuario()
    return render(request, 'registro.html', {'formulario': formulario})

@user_passes_test(es_admin)
def crear_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            messages.success(request, f'Usuario {"técnico" if usuario.es_tecnico else "cliente"} creado exitosamente.')
            return redirect('inicio')
    else:
        formulario = UsuarioForm()
    return render(request, 'crear_usuario.html', {'formulario': formulario})

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
                try:
                    usuario_personalizado = Usuario.objects.get(correo_electronico=usuario.email)
                    if usuario_personalizado.es_tecnico:
                        return redirect('inicio_tecnico')
                    else:
                        return redirect('inicio_cliente')
                except Usuario.DoesNotExist:
                    messages.error(request, 'No se encontró un perfil de usuario asociado.')
                    return redirect('login.html')
            else:
                messages.error(request, 'Nombre de usuario o contraseña inválidos')
    else:
        formulario = FormularioLogin()
    return render(request, 'login.html', {'formulario': formulario})

@login_required
def inicio(request):
    try:
        usuario = Usuario.objects.get(correo_electronico=request.user.email)
        if usuario.es_tecnico:
            return redirect('inicio_tecnico')
        else:
            return redirect('inicio_cliente')
    except Usuario.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de usuario asociado.')
        return redirect('login')

