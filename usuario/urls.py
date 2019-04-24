from django.conf.urls import url
from usuario.views import *

urlpatterns = [
	url(r'^perfil', perfil, name='usuario_perfil'),
	url(r'^users_list', users_list, name='users_list'),
    url(r'^users_create', users_create, name='users_create'),
    url(r'^users_insert', users_insert, name='users_insert'),
    url(r'^users_delete', users_delete, name='users_delete'),
    url(r'^users_get', users_get, name='users_get'),
    url(r'^users_update', users_update, name='users_update'),
]