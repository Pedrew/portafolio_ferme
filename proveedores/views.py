from django.shortcuts import render
from .models import Proveedor
from django.shortcuts import redirect

# Create your views here.

def proveedores_list(request):
	proveedor_list = Proveedor.getProveedores()
	return render(request, 'proveedores/proveedores_list.html',{ 'proveedores' : proveedor_list})

def proveedores_create(request):
	return render(request, 'proveedores/proveedores_create.html')

def proveedores_insert(request):
	post = request.POST
	nombre = post['nombre']
	rut = post['rut']
	mail = post['mail']
	telefono = post['telefono']
	Proveedor.createProveedor(nombre, rut, mail, telefono)
	response = redirect('proveedores_list')
	return response 