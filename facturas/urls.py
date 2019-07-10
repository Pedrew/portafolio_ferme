from django.conf.urls import url
from facturas.views import *

urlpatterns = [
	url(r'^facturas_list', facturas_list, name='facturas_list'),
    url(r'^factura_detail', factura_detail, name='factura_detail'),
]