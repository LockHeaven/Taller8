from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('',home,name = 'index'),
    path('crear_usuario/',crearUsuario,name = 'crear_usuario'),
    path('listar_usuario/',listarUsuario,name = 'listar_usuario'),
    #path('editar_usuario/<int:id>',editarUsuario, name = 'editarUsuario'),
    re_path(r'^editar_usuario/(?P<id>\d+)/$',editarUsuario, name = 'editar_usuario'),
]