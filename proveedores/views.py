from django.shortcuts import render
from .models import Proveedores
from django.shortcuts import redirect

# Create your views here.

def proveedor_list(request):
	proveedor_list = Proveedor.getProveedores()
	return render(request, 'proveedor/proveedores_list.html',{ 'proveedores' : proveedor_list})
