from django.urls import path

from . import views

urlpatterns = [
    path('usuarios', views.MuestraUsuarios, name='index'),
    path('', views.CreaUsuarios),
]