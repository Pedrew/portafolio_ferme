from django.conf.urls import url
from orden_compra.views import *

urlpatterns = [
	url(r'^orders_list', orders_list, name='orders_list'),
    url(r'^orders_create', orders_create, name='orders_create'),
    url(r'^orders_insert', orders_insert, name='orders_insert'),
]