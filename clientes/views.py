from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gestor.models import Ticket, Usuario
from gestor.forms import TicketForm

@login_required
def listar_tickets_clientes(request):
    try:
        usuario = Usuario.objects.get(correo_electronico=request.user.email)
        tickets = Ticket.objects.filter(id_usuario=usuario)
        return render(request, 'clientes/inicio_cliente.html', {'tickets': tickets})
    except Usuario.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de usuario asociado.')
        return redirect('inicio')

@login_required
def crear_tickets_cliente(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            try:
                usuario_actual = Usuario.objects.get(correo_electronico=request.user.email)
                ticket.id_usuario = usuario_actual
                ticket.save()
                messages.success(request, 'TICKET CREADO CORRECTAMENTE')
                return redirect('listar_ticket_cliente')
            except Usuario.DoesNotExist:
                messages.error(request, 'No se encontró un perfil de usuario asociado.')
        else:
            messages.error(request, 'HUBO UN ERROR AL CREAR EL TICKET. POR FAVOR VERIFICA LOS DATOS.')
    else:
        form = TicketForm()
    return render(request, 'clientes/crear_ticket.html', {'form': form})

@login_required
def inicio_cliente(request):
    try:
        usuario = Usuario.objects.get(correo_electronico=request.user.email)
        tickets = Ticket.objects.filter(id_usuario=usuario)
        return render(request, "clientes/inicio_cliente.html", {'tickets': tickets})
    except Usuario.DoesNotExist:
        messages.error(request, 'No se encontró un perfil de usuario asociado.')
        return redirect('login')