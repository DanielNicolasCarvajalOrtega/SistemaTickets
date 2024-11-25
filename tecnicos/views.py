from django.shortcuts import render, redirect
from django.contrib import messages
from gestor.models import Ticket
from gestor.forms import TicketForm


def listar_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/listar_tickets.html', {'tickets': tickets})


def crear_tickets(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'TICKET CREADO CORRECTAMENTE')
            return redirect('listar_tickets')

    else:
        form = TicketForm()
    return render(request,'insertar_tickets.html', {'form': form})



def actualizar_tickets(request):
    if request.method == "POST":
        