from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('acerca/', views.about, name = 'acerca'),
    path('', views.index, name = 'indice' ),
    path('bienvenido/', views.welcome, name = 'bienvenido'),
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('receta/', views.receta, name='receta')
]
