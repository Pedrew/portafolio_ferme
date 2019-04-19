from django.shortcuts import render
from .models import Product

# Create your views here.
product_list = Product.getProductos()

def productos_list(request):
	return render(request, 'productos/product_list.html',{ 'productos' : product_list})
