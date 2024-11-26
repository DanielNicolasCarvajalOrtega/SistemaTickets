from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.listar_tickets, name='listar_tickets'),
    path('tickets/actualizar/<int:ticket_id>/', views.actualizar_tickets, name='actualizar_tickets'),
    path('tickets/eliminar/<int:ticket_id>/', views.eliminar_tickets, name='eliminar_tickets'),
]