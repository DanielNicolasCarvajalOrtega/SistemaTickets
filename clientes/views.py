from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gestor.models import Ticket
from gestor.forms import TicketForm
from gestor.models import Cliente


@login_required
def listar_tickets_clientes(request):
    tickets = Ticket.objects.filter(id_cliente=request.user.Cliente)
    return render(request, 'clientes/listar_ticket_cliente.html', {'tickets': tickets})


@login_required
def crear_tickets_cliente(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            try:
                cliente_actual = Cliente.objects.get(correo_electronico=request.user.email)
                ticket.id_cliente = cliente_actual
                ticket.save()
                messages.success(request, 'TICKET CREADO CORRECTAMENTE')
                return redirect('listar_ticket_cliente')
            except Cliente.DoesNotExist:
                messages.error(request, 'No se encontró un cliente asociado con tu usuario.')
        else:
            messages.error(request, 'HUBO UN ERROR AL CREAR EL TICKET. POR FAVOR VERIFICA LOS DATOS.')
    else:
        form = TicketForm()
    return render(request, 'crear_ticket.html', {'form': form})

@login_required
def inicio_cliente(request):
    
    return render(request,"inicio.html")