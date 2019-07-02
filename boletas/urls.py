from django.conf.urls import url
from boletas.views import *

urlpatterns = [
	url(r'^boletas_list', boletas_list, name='boletas_list'),
    url(r'^boleta_detail', boleta_detail, name='boleta_detail'),
]