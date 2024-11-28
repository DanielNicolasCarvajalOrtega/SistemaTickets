from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio_cliente,name="inicio_cliente"),
    path('crear_ticket/', views.crear_tickets_cliente, name="crear_ticket_cliente"),
    path('listar_ticket/', views.listar_tickets_clientes, name="listar_ticket_cliente"),
]


