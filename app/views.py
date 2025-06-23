from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # <-- AÑADIR ESTE IMPORT

from .forms import RegisterForm, LoginForm, CredencialForm
from .models import Credencial

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_menu')
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('main_menu')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_menu')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

@login_required
def main_menu_view(request):
    return render(request, 'app/main_menu.html')

@login_required
def auth_view(request):
    return render(request, 'app/agregar.html')

@login_required
def organization_view(request):
    return render(request, 'app/ver.html')

def logout_view(request):
    logout(request)
    return redirect('login')


# --- VISTA UNIFICADA (ACTUALIZADA CON EL MENSAJE) ---
@login_required
def agregar_credencial_view(request, categoria):
    nombres_categorias = {
        'banco': 'Banco',
        'red_social': 'Red Social',
        'correo': 'Correo Electrónico'
    }
    if categoria not in nombres_categorias:
        return redirect('main_menu')

    if request.method == 'POST':
        form = CredencialForm(request.POST, categoria=categoria)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.usuario_propietario = request.user
            instancia.categoria = categoria
            instancia.save()
            
            # --- LÍNEA CLAVE AÑADIDA ---
            # Creamos un mensaje de éxito que se mostrará en la siguiente página.
            messages.success(request, '¡Tu contraseña se ha guardado correctamente!')
            
            return redirect('main_menu')
    else:
        form = CredencialForm(categoria=categoria)

    contexto = {
        'form': form,
        'titulo_pagina': f"Agregar Contraseña de {nombres_categorias[categoria]}"
    }
    return render(request, 'app/agregar_formulario.html', contexto)