from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from gestor.models import Ticket
from gestor.forms import TicketForm

@login_required
def listar_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/listar_tickets.html', {'tickets': tickets})


@login_required
def actualizar_tickets(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'TICKET ACTUALIZADO CORRECTAMENTE')
            return redirect('listar_tickets')
        else:
            messages.error(request, 'HUBO UN ERROR AL ACTUALIZAR EL TICKET. POR FAVOR VERIFICA LOS DATOS.')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/actualizar_tickets.html', {'form': form})

@login_required
def eliminar_tickets(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        ticket.delete()
        messages.success(request, 'TICKET ELIMINADO CORRECTAMENTE')
        return redirect('listar_tickets')
    return render(request, 'tickets/eliminar_tickets.html', {'ticket': ticket})
