from django.contrib import admin
from .models import Rol, Usuario, Ticket, TicketAsignado

class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nom_rol')
    search_fields = ['nom_rol']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'correo_electronico', 'telefono', 'id_rol', 'es_tecnico')
    list_filter = ('es_tecnico', 'id_rol')
    search_fields = ['nombre', 'correo_electronico']

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id_ticket', 'descripcion', 'estado', 'id_usuario')
    list_filter = ('estado',)
    search_fields = ['descripcion']
    raw_id_fields = ['id_usuario']

class TicketAsignadoAdmin(admin.ModelAdmin):
    list_display = ('id_ticket', 'id_tecnico')
    raw_id_fields = ['id_ticket', 'id_tecnico']

admin.site.register(Rol, RolAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketAsignado, TicketAsignadoAdmin)