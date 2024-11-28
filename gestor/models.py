from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nom_rol = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.nom_rol

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128)
    correo_electronico = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=11, blank=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    es_tecnico = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    @classmethod
    def crear_usuario(cls, nombre_usuario, correo, contraseña, es_tecnico=False):
        usuario_auth = User.objects.create_user(nombre_usuario, correo, contraseña)
        usuario = cls.objects.create(
            nombre=nombre_usuario,
            correo_electronico=correo,
            contraseña=make_password(contraseña),
            id_rol_id=2 if es_tecnico else 1,  # Asumimos que 1 es para clientes y 2 para técnicos
            es_tecnico=es_tecnico
        )
        return usuario_auth, usuario

class Ticket(models.Model):
    # Definimos los estados posibles del ticket
    ESTADO_OPCIONES = [
        ('abierto', 'Abierto'),
        ('en_proceso', 'En Proceso'),
        ('cerrado', 'Cerrado'),
    ]
    
    id_ticket = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_OPCIONES,
        default='abierto',
    )
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket #{self.id_ticket} - {self.estado}"

class TicketAsignado(models.Model):
    id_ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    id_tecnico = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'es_tecnico': True})

    def __str__(self):
        return f"Ticket #{self.id_ticket.id_ticket} asignado a {self.id_tecnico.nombre}"

