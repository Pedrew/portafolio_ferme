from django.conf.urls import url
from reportes.views import *

urlpatterns = [
	url(r'^reportes', reportes, name='reportes'),
	url(r'^boletas_anno', boletas_anno, name='boletas_anno'),
]