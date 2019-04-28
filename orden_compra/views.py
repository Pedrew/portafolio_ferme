from django.shortcuts import render
from .models import Orders
from django.shortcuts import redirect
import datetime

# Create your views here.
def orders_list(request):
	order_list = Orders.getOrders()
	proveedores_list = Orders.getProveedores()
	return render(request, 'orden_de_compra/orders_list.html',{ 'order_list' : order_list, 'proveedores_list': proveedores_list})

def orders_create(request):

	return render(request, 'orden_de_compra/order_create.html', { 'prov_id' : '', 'tipo': '', 'familia': '', 'tipo_id': '' })

def orders_insert(request):

	response = redirect('orders_list')
	return response