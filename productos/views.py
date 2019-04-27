from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect
import datetime

# Create your views here.

def productos_list(request):
	product_list = Product.getProductos()
	return render(request, 'productos/product_list.html',{ 'productos' : product_list})

def productos_create(request):
	proveedor_list = Product.getProveedores()
	return render(request, 'productos/product_create.html', { 'proveedores' : proveedor_list})

def productos_insert(request):
	post = request.POST
	nombre = post['nombre']
	valor = post['valor']
	stock = post['stock']
	stock_critico = post['stock_critico']
	codigo_tipo = post['codigo_tipo']
	proveedor_id = post['proveedor_id']
	familia = post['familia']
	fecha_vencimiento = post['fecha_de_vencimiento']
	if fecha_vencimiento == "":
		fecha_vencimiento = "00000000"
	tipo = post['tipo']
	
	producto_id = proveedor_id + familia + fecha_vencimiento.replace("-", "") + tipo

	Product.createProduct(producto_id, nombre, valor, stock, stock_critico, codigo_tipo)
	response = redirect('productos_list')
	return response

def productos_delete(request):
	get = request.GET
	product_id = get['id']
	Product.deleteProduct(product_id)
	response = redirect('productos_list')
	return response

def productos_get(request):
	get = request.GET
	product_id = get['id']
	response = Product.getProduct(product_id)
	return render(request, 'productos/product_update.html',{'product':response})

def productos_update(request):
	post = request.POST
	producto_id = post['producto_id']
	nombre = post['nombre']
	valor = post['valor']
	stock = post['stock']
	stock_critico = post['stock_critico']
	Product.updateProduct(producto_id, nombre, valor, stock, stock_critico)
	response = redirect('productos_list')
	return response



def familia_list(request):
	proveedor_list = Product.getProveedores()
	familia_list = Product.getFamilias()
	tipo_list = Product.getTipos()
	return render(request, 'productos/family_type.html',{ 'familia' : familia_list, 'tipo' : tipo_list, 'proveedores' : proveedor_list})

def familia_create(request):
	post = request.POST
	proveedor_id = post['proveedor_id']
	return render(request, 'productos/family_create.html',{'proveedor':proveedor_id})

def familia_insert(request):
	post = request.POST
	identificador = post['identificador']
	detalle = post['detalle']
	id_proveedor = post['id_proveedor']
	Product.createFamilia(identificador, detalle, id_proveedor)
	response = redirect('familia_list')
	return response

def tipo_create(request):
	get = request.GET
	family_id = get['id']
	family_name = get['family']
	return render(request, 'productos/type_create.html',{ 'family_id' : family_id, 'family_name' : family_name})

def tipo_insert(request):
	post = request.POST
	identificador = post['identificador']
	detalle = post['detalle']
	id_familia = post['id_familia']
	Product.createTipo(identificador, detalle, id_familia)
	response = redirect('familia_list')
	return response
	