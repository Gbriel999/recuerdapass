from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# --- MODELO DE USUARIO PERSONALIZADO (YA LO TENÍAS) ---
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


# --- NUEVO MODELO UNIFICADO PARA TODAS LAS CONTRASEÑAS (SIN ENCRIPTACIÓN) ---
class Credencial(models.Model):
    # Opciones para el campo 'categoría'
    CATEGORIA_CHOICES = [
        ('banco', 'Banco'),
        ('red_social', 'Red Social'),
        ('correo', 'Correo Electrónico'),
    ]

    # --- CAMPOS DE LA TABLA ---
    usuario_propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    nombre_servicio = models.CharField("Nombre del Servicio/Plataforma", max_length=100)
    identificador_usuario = models.CharField("Email o Nombre de Usuario", max_length=255)
    
    # La contraseña se guarda como texto plano en un CharField
    contrasena = models.CharField("Contraseña", max_length=255)

    def __str__(self):
        # Texto que aparecerá en el panel de administración de Django
        return f"{self.get_categoria_display()}: {self.nombre_servicio} ({self.usuario_propietario.username})"