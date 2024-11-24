from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nom_rol = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.nom_rol


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=11)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre