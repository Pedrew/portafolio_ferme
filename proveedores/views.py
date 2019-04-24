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

def proveedores_get(request):
	get = request.GET
	proveedor_id = get['id']
	response = Proveedor.getProveedor(proveedor_id)
	return render(request, 'proveedores/proveedores_update.html',{'proveedor':response})

def proveedores_update(request):
	post = request.POST
	proveedor_id = post['proveedor_id']
	nombre = post['nombre']
	rut = post['rut']
	mail = post['mail']
	telefono = post['telefono']
	Proveedor.updateProveedor(proveedor_id, nombre, rut, mail, telefono)
	response = redirect('proveedores_list')
	return response

