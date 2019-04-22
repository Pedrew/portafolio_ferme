from django.conf.urls import url
from productos.views import *

urlpatterns = [
	url(r'^productos_list', productos_list, name='productos_list'),
    url(r'^productos_create', productos_create, name='productos_create'),
    url(r'^productos_insert', productos_insert, name='productos_insert'),
    url(r'^productos_delete', productos_delete, name='productos_delete'),
]