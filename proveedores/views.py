from django.shortcuts import render
from .models import Proveedor
from django.shortcuts import redirect

# Create your views here.

def proveedores_list(request):
	
	proveedor_list = Proveedor.getProveedores()
	return render(request, 'proveedores/proveedores_list.html',{ 'proveedores' : proveedor_list})
