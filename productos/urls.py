from django.conf.urls import url
from productos.views import *

urlpatterns = [
	url(r'^productos_ferreteria_list', productos_ferreteria_list, name='productos_ferreteria_list'),
    url(r'^productos_ferreteria_create', productos_ferreteria_create, name='productos_ferreteria_create'),
    url(r'^productos_ferreteria_insert', productos_ferreteria_insert, name='productos_ferreteria_insert'),
    url(r'^productos_ferreteria_delete', productos_ferreteria_delete, name='productos_ferreteria_delete'),
    url(r'^productos_ferreteria_get', productos_ferreteria_get, name='productos_ferreteria_get'),
    url(r'^productos_ferreteria_update', productos_ferreteria_update, name='productos_ferreteria_update'),
    url(r'^productos_sell_list', productos_sell_list, name='productos_sell_list'),
]