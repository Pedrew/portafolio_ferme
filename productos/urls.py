from django.conf.urls import url
from productos.views import *

urlpatterns = [
	url(r'^productos_list', productos_list, name='productos_list'),
    url(r'^productos_create', productos_create, name='productos_create'),
    url(r'^productos_insert', productos_insert, name='productos_insert'),
    url(r'^productos_delete', productos_delete, name='productos_delete'),
    url(r'^productos_get', productos_get, name='productos_get'),
    url(r'^productos_update', productos_update, name='productos_update'),


    url(r'^familia_list', familia_list, name='familia_list'),
    url(r'^familia_create', familia_create, name='familia_create'),
    url(r'^familia_insert', familia_insert, name='familia_insert'),
    url(r'^tipo_create', tipo_create, name='tipo_create'),
    url(r'^tipo_insert', tipo_insert, name='tipo_insert'),
]