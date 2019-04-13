from django.conf.urls import url
from usuario.views import perfil

urlpatterns = [
	url(r'^perfil', perfil, name='usuario_perfil'),
]