from django.contrib import admin
from .models import Cliente, Tecnico, Rol, Ticket, TicketAsignado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'correo_electronico', 'telefono', 'id_rol')
    search_fields = ('nombre', 'correo_electronico')

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('id_tecnico', 'nombre', 'correo_electronico', 'telefono', 'id_rol')
    search_fields = ('nombre', 'correo_electronico')

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nom_rol')  # Cambié 'id' por 'id_rol'
    search_fields = ('nom_rol',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id_ticket', 'descripcion', 'estado', 'id_cliente')  # Cambié 'id' por 'id_ticket'
    search_fields = ('descripcion',)

@admin.register(TicketAsignado)
class TicketAsignadoAdmin(admin.ModelAdmin):
    list_display = ('id_ticket', 'id_tecnico')  # Cambié 'id' por 'id_ticket'
    search_fields = ('id_ticket__descripcion', 'id_tecnico__nombre')
