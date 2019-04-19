from django.conf.urls import url
from productos.views import productos_list

urlpatterns = [
	url(r'^productos_list', productos_list, name='productos_list'),
    
]