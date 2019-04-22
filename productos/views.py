from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect

# Create your views here.

def productos_list(request):
	product_list = Product.getProductos()
	return render(request, 'productos/product_list.html',{ 'productos' : product_list})

def productos_create(request):
	return render(request, 'productos/product_create.html')

def productos_insert(request):
	post = request.POST
	nombre = post['nombre']
	valor = post['valor']
	Product.createProduct(nombre, valor)
	response = redirect('productos_list')
	return response

def productos_delete(request):
	get = request.GET
	product_id = get['id']
	Product.deleteProduct(product_id)
	response = redirect('productos_list')
	return response