from django.shortcuts import render
from productos.models import Product

# Create your views here.
def home(request):
	product_list = Product.getProductos()
	return render(request, 'home/index.html',{ 'productos' : product_list})

def productos(request):
	return render(request, 'productos/product_list.html')

def proveedores(request):
	return render(request, 'proveedores/proveedores_list.html')	