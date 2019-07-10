from django.shortcuts import render
from .models import Orders
from django.shortcuts import redirect
import datetime

# Create your views here.
def orders_list(request):
	get = request.GET
	proveedor = get['proveedor']
	tipo = get['tipo']
	order_list = Orders.getOrders(proveedor, tipo)
	proveedores_list = Orders.getProveedores()
	return render(request, 'orden_de_compra/orders_list.html',{
		'order_list' : order_list,
		'proveedores_list': proveedores_list,
		'proveedor': proveedor,
		'tipo' : tipo
	})

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
	user_tipo = post['user_tipo']
	valor = post['total']
	estado = 1
	stock = post['stock']
	stock_crit = post['stock_crit']

	Orders.createOrder(id_prov, id_prod, id_user, valor, estado, stock, stock_crit)

	response = redirect('/orden_de_compra/orders_list?proveedor='+(str(1))+'&tipo='+user_tipo)
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
	id_user = post['id_user']
	estado = post['estado']
	user_tipo = post['id_tipo']
	id_orden = post['id_orden']
	if estado == "4":
		id_prov = post['id_prov']
		id_prod = post['id_prod']
		stock = post['stock']
		stock_crit = post['stock_crit']
		Orders.createProduct(id_prov, id_prod, stock, stock_crit)
		Orders.updateOrder(id_orden, estado)
	else:
		Orders.updateOrder(id_orden, estado)
	return redirect('/orden_de_compra/orders_list?proveedor='+(str(id_user))+'&tipo='+user_tipo)
