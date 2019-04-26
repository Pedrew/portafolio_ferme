from django.conf.urls import url
from proveedores.views import *

urlpatterns = [
	url(r'^proveedores_list', proveedores_list, name='proveedores_list'),
]