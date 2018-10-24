from django.urls import path
from .views import *

urlpatterns = [
    path('',actor_lista_view,name='actor_lista'),
    path('cliente/',cliente_lista_view,name='cliente_lista'),
    path('director/',director_lista_view,name='director_lista'),
    path('formato/',formato_lista_view,name='formato_lista'),
    path('genero/',genero_lista_view,name='genero_lista'),
    path('video/',video_lista_view,name='video_lista'),
    path('alquiler/',alquiler_lista_view,name='alquiler_lista'),
    path('listado/',listado_lista_view,name='listado_lista'),
    path('mas_premiada/',mas_premiada_view,name='mas_premiada'),
    path('consulta/',consulta_view,name='consulta'),
    
    path('eliminar_actor/<int:pk>/',eliminar_actor_view,name='eliminar_actor'),
    path('agregar_actor/',agregar_actor_view,name='agregar_actor'),
    
]

# Actor
# Listado
# Cliente
# Director
# Formato
# Genero
# Video
# Alquiler
# VideoHasGenero
# ActorHasVideo