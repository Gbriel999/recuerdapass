from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('main/', views.main_menu_view, name='main_menu'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar/', views.auth_view, name='auth'),
    path('agregar/<str:categoria>/', views.agregar_credencial_view, name='agregar_credencial'),
    path('ver/', views.organization_view, name='organization'),
]
