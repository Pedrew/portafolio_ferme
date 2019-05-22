"""ferme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout, login
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^usuario/', include('usuario.urls')),
    url(r'^usuario/', include('django.contrib.auth.urls')),
    url(r'^login', login, name="login"),
    url(r'^logout', logout, name="logout"),
    url(r'^productos_proveedor/', include('productos_proveedor.urls')),
    url(r'^proveedores/', include('proveedores.urls')),
    url(r'^orden_de_compra/', include('orden_compra.urls')),
    url(r'^productos_ferreteria/', include('productos.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)