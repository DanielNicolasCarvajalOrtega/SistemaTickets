from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from gestor.models import Ticket, Usuario
from gestor.forms import TicketForm

def es_tecnico(user):
    try:
        return Usuario.objects.get(correo_electronico=user.email).es_tecnico
    except Usuario.DoesNotExist:
        return False

@login_required
@user_passes_test(es_tecnico)
def inicio_tecnico(request):
    tickets_abiertos = Ticket.objects.filter(estado='abierto').count()
    tickets_en_proceso = Ticket.objects.filter(estado='en_proceso').count()
    tickets_cerrados = Ticket.objects.filter(estado='cerrado').count()
    
    context = {
        'tickets_abiertos': tickets_abiertos,
        'tickets_en_proceso': tickets_en_proceso,
        'tickets_cerrados': tickets_cerrados,
    }
    return render(request, 'tecnicos/inicio_tecnico.html', context)

@login_required
@user_passes_test(es_tecnico)
def listar_tickets(request):
    tickets = Ticket.objects.all().order_by('id_usuario')
    return render(request, 'tecnicos/listar_tickets.html', {'tickets': tickets})

@login_required
@user_passes_test(es_tecnico)
def detalle_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tecnicos/detalle_ticket.html', {'ticket': ticket})

@login_required
@user_passes_test(es_tecnico)
def actualizar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket actualizado correctamente.')
            return redirect('tecnicos:detalle_ticket', ticket_id=ticket.id)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tecnicos/actualizar_ticket.html', {'form': form, 'ticket': ticket})

@login_required
@user_passes_test(es_tecnico)
def cerrar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        ticket.estado = 'cerrado'
        ticket.save()
        messages.success(request, 'Ticket cerrado correctamente.')
        return redirect('tecnicos:listar_tickets')
    return render(request, 'tecnicos/cerrar_ticket.html', {'ticket': ticket})

@login_required
@user_passes_test(es_tecnico)
def estadisticas(request):
    total_tickets = Ticket.objects.count()
    tickets_abiertos = Ticket.objects.filter(estado='abierto').count()
    tickets_en_proceso = Ticket.objects.filter(estado='en_proceso').count()
    tickets_cerrados = Ticket.objects.filter(estado='cerrado').count()
    
    context = {
        'total_tickets': total_tickets,
        'tickets_abiertos': tickets_abiertos,
        'tickets_en_proceso': tickets_en_proceso,
        'tickets_cerrados': tickets_cerrados,
    }
    return render(request, 'tecnicos/estadisticas.html', context)

