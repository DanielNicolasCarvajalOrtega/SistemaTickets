from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_tecnico, name='inicio_tecnico'),
    path('tickets/', views.listar_tickets, name='listar_tickets'),
    path('tickets/<int:ticket_id>/', views.detalle_ticket, name='detalle_ticket'),
    path('tickets/<int:ticket_id>/actualizar/', views.actualizar_ticket, name='actualizar_ticket'),
    path('tickets/<int:ticket_id>/cerrar/', views.cerrar_ticket, name='cerrar_ticket'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
]

