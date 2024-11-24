from django.db import models
from Clientes.models import Cliente,Rol

class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=11)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Ticket(models.Model):
    # Definimos los estados posibles del ticket
    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('en_proceso', 'En Proceso'),
        ('cerrado', 'Cerrado'),
    ]

    id_ticket = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='abierto',
    )
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket #{self.id_ticket} - {self.estado}"


class TicketAsignado(models.Model):
    id_ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket #{self.id_ticket.id_ticket} asignado a {self.id_tecnico.nombre}"

