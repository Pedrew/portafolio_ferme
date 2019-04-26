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

	proveedor_id = post['proveedor_id']
	familia = post['familia']
	fecha_vencimiento = post['fecha_de_vencimiento']
	if fecha_vencimiento == "":
		fecha_vencimiento = "00000000"
	tipo = post['tipo']
	
	producto_id = proveedor_id + familia + fecha_vencimiento.replace("-", "") + tipo

	Product.createProduct(producto_id, nombre, valor, stock, stock_critico)
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
	