from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nom_rol = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.nom_rol

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128) 
    correo_electronico = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=11)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, default=1)  

    def __str__(self):
        return self.nombre

    @classmethod
    def crear_usuario(cls, nombre_usuario, correo, contraseña):
        # Crear usuario en el sistema de autenticación
        usuario = User.objects.create_user(nombre_usuario, correo, contraseña)
        # Crear cliente asociado con contraseña hasheada
        cliente = cls.objects.create(
            nombre=nombre_usuario,
            correo_electronico=correo,
            contraseña=make_password(contraseña),  
            telefono='',  #
            id_rol_id=1  
        )
        return usuario, cliente

class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128)  # Incrementamos el tamaño para contraseñas hasheadas
    correo_electronico = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=11)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    @classmethod
    def crear_tecnico(cls, nombre_tecnico, correo, contraseña, id_rol=2):  # Supongamos que 2 es el rol por defecto para técnicos
        tecnico = cls.objects.create(
            nombre=nombre_tecnico,
            correo_electronico=correo,
            contraseña=make_password(contraseña),  # Hashear la contraseña
            telefono='',  # Puede dejarse vacío inicialmente
            id_rol_id=id_rol
        )
        return tecnico

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
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket #{self.id_ticket} - {self.estado}"

class TicketAsignado(models.Model):
    id_ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket #{self.id_ticket.id_ticket} asignado a {self.id_tecnico.nombre}"

