from django.urls import path, include
from  . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('listar_alumnos/', views.Mostrar_alumnos, name='listar_alumnos'),
    
]
