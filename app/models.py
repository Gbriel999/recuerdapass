from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Credencial(models.Model):
    CATEGORIA_CHOICES = [
        ('banco', 'Banco'),
        ('red_social', 'Red Social'),
        ('correo', 'Correo Electrónico'),
    ]
    usuario_propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    nombre_servicio = models.CharField("Nombre del Servicio/Plataforma", max_length=100)
    identificador_usuario = models.CharField("Email o Nombre de Usuario", max_length=255)
    contrasena = models.CharField("Contraseña", max_length=255)

    def __str__(self):
        return f"{self.get_categoria_display()}: {self.nombre_servicio} ({self.usuario_propietario.username})"
