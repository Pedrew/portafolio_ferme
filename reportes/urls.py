from django.conf.urls import url
from reportes.views import *

urlpatterns = [
	url(r'^reportes', reportes, name='reportes'),
	url(r'^boletas_anno', boletas_anno, name='boletas_anno'),
    url(r'^boletas_mes', boletas_mes, name='boletas_mes'),
    url(r'^boletas_dia', boletas_dia, name='boletas_dia'),
    url(r'^compras_usuario', compras_usuario, name='compras_usuario'),
    url(r'^compras_metodo', compras_metodo, name='compras_metodo'),
    url(r'^compras_lugar', compras_lugar, name='compras_lugar'),
]