from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Credencial

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class CredencialForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    def __init__(self, *args, **kwargs):
        categoria = kwargs.pop('categoria', None)
        super().__init__(*args, **kwargs)
        if categoria:
            # Opcional: puedes filtrar campos o hacer algo según categoría aquí
            pass

    class Meta:
        model = Credencial
        fields = ['nombre_servicio', 'identificador_usuario', 'contrasena']
