from django.conf.urls import url
from orden_compra.views import *

urlpatterns = [
	url(r'^orders_list', orders_list, name='orders_list'),
    url(r'^orders_create', orders_create, name='orders_create'),
    url(r'^orders_insert', orders_insert, name='orders_insert'),
    url(r'^productos_get', productos_get, name='productos_get'),
    url(r'^order_status', order_status, name='order_status'),
    url(r'^order_update', order_update, name='order_update'),
]