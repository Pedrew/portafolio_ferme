from django.conf.urls import url
from proveedores.views import *

urlpatterns = [
	url(r'^proveedores_list', proveedores_list, name='proveedores_list'),
	url(r'^proveedores_create', proveedores_create, name='proveedores_create'),
	url(r'^proveedores_insert', proveedores_insert, name='proveedores_insert'),
]