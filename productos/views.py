from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect
import datetime


# Create your views here.

def productos_ferreteria_list(request):
	product_list = Product.getProductos()
	return render(request, 'productos_ferreteria/product_list.html',{ 'productos' : product_list})

def productos_ferreteria_create(request):
	get = request.GET
	proveedor_id = get['id_prov']
	tipo = get['tipo']
	familia = get['familia']
	tipo_id = get['id_tipo']
	proveedor_id = Product.getProveedorId(proveedor_id)
	return render(request, 'productos_ferreteria/product_create.html', { 'prov_id' : proveedor_id, 'tipo': tipo, 'familia': familia, 'tipo_id': tipo_id })

def productos_ferreteria_insert(request):
	post = request.POST
	nombre = post['nombre']
	valor = post['valor']

	codigo_tipo = post['tipo']
	proveedor_id = post['proveedor_id']
	
	prov_id = post['prov_id']
	familia = post['familia']
	
	fecha_vencimiento = post['fecha_de_vencimiento']
	if fecha_vencimiento == "":
		fecha_vencimiento = "00000000"
	tipo = post['tipo_id']
	
	producto_id = proveedor_id + familia + fecha_vencimiento.replace("-", "") + codigo_tipo

	Product.createProduct(producto_id, nombre, valor, tipo, prov_id)
	response = redirect('productos_ferreteria_list')
	return response

def productos_ferreteria_delete(request):
	get = request.GET
	product_id = get['id']
	Product.deleteProduct(product_id)
	response = redirect('productos_ferreteria_list')
	return response

def productos_ferreteria_get(request):
	get = request.GET
	product_id = get['id']
	response = Product.getProduct(product_id)
	return render(request, 'productos_ferreteria/product_update.html',{'product':response})

def productos_ferreteria_update(request):
	post = request.POST
	producto_id = post['producto_id']
	nombre = post['nombre']
	valor = post['valor']
	Product.updateProduct(producto_id, nombre, valor)
	response = redirect('productos_ferreteria_list')
	return response

def productos_sell_list(request):
	product_list = Product.getProductos()
	return render(request, 'productos_ferreteria/product_sell_list.html',{ 'productos' : product_list})

def productos_detail(request):
	get = request.GET
	product_id = get['id']
	tipo = get['tipo']
	response = Product.getProduct(product_id)
	familia_tipo = Product.getTipo(tipo)
	return render(request, 'productos_ferreteria/product_detail.html',{'product':response, 'tipo':familia_tipo})

def product_receipt(request):
	post = request.POST
	cantidad = post['cantidad']
	id = post['id']

	Product.updateStock(id, cantidad)

	id_user = post['id_user']
	entrega = post['entrega']
	pago_tipo = post['payment_type']
	medio_pago = post['payment_method']
	total = post['total']
	
	now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

	Product.createBoleta(id_user, pago_tipo, medio_pago, entrega, now, id, cantidad, total)

	detalle = Product.getDetalle(id)
	usuario = Product.getUser(id_user)
	boleta = Product.getLastBoleta(id_user)
	return render(request, 'productos_ferreteria/product_receipt.html', {'detalle': detalle, 'usuario': usuario, 'boleta': boleta, 'entrega': entrega, 'pago_tipo': pago_tipo, 'medio_pago': medio_pago})

def shopping_cart(request):
	post = request.POST
	cantidad = post['cantidad']
	id = post['id']
	valor = post['precio']
	total = int(cantidad) * int(valor)
	product = Product.getProduct(id)
	
	return render(request, 'productos_ferreteria/shopping_cart.html', {'product': product, 'total': total, 'cantidad': cantidad})
