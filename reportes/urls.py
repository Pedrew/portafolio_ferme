from django.conf.urls import url
from reportes.views import *

urlpatterns = [
	url(r'^boletas_anno', boletas_anno, name='boletas_anno'),
]