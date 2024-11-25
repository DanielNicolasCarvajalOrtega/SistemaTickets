from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.inicio_sesion, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.inicio_sesion, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]