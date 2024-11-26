from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("gestor.urls")),
    path("cliente/", include("clientes.urls")),
    path("tecnico/", include("tecnicos.urls")),
]
