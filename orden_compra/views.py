from django.shortcuts import render
from .models import Orders
from django.shortcuts import redirect
import datetime

# Create your views here.
def orders_list(request):
	get = request.GET
	proveedor_id = get['id']
	order_list = Orders.getOrders(proveedor_id)
	proveedores_list = Orders.getProveedores()
	return render(request, 'orden_de_compra/orders_list.html',{ 'order_list' : order_list, 'proveedores_list': proveedores_list})

def productos_get(request):
	get = request.GET
	product_id = get['id']
	proveedor = get['proveedor']
	response = Orders.getProductos(product_id)
	return render(request, 'orden_de_compra/products_list.html',{'productos':response, 'proveedor':proveedor, 'id_prov':product_id})

def orders_insert(request):
	post = request.POST
	id_prov = post['id_prov']
	id_prod = post['id_prod']
	id_user = post['id_user']
	valor = post['total']
	estado = 1
	stock = post['stock']
	stock_crit = post['stock_crit']

	Orders.createOrder(id_prov, id_prod, id_user, valor, estado, stock, stock_crit)

	response = redirect('orders_list')
	return response

def orders_create(request):
	get = request.GET
	product_id = get['id']
	prov_id = get['id_prov']
	prov = get['prov']
	nombre = get['producto']
	valor = get['valor']
	response = Orders.getProductos(product_id)
	return render(request, 'orden_de_compra/order_create.html',{'products':response, 'prov_id':prov_id, 'prov':prov, 'nombre':nombre, 'valor':valor, 'id_prod':product_id})

def order_status(request):
	get = request.GET
	order_id = get['id']
	response = Orders.getOrder(order_id)
	return render(request, 'orden_de_compra/order_status.html',{'orden':response})

def order_update(request):
	post = request.POST
	estado = post['estado']
	id_orden = post['id_orden']
	if estado == "4":
		id_prov = post['id_prov']
		id_prod = post['id_prod']
		stock = post['stock']
		stock_crit = post['stock_crit']
		Orders.createProduct(id_prov, id_prod, stock, stock_crit)
		Orders.updateOrder(id_orden, estado)
		response = redirect('orders_list')
	else:
		Orders.updateOrder(id_orden, estado)
		response = redirect('orders_list')
	return response
