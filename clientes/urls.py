from django.urls import path
from . import views

urlpatterns = [
    path("inicio_cliente/",views.inicio_cliente,name="inicio"),
    path('crear_ticket/', views.crear_tickets_cliente, name="crear_ticket_cliente"),
    path('listar_ticket/', views.listar_tickets_clientes, name="listar_ticket_cliente"),
]


