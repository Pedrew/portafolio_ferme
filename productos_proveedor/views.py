from django.shortcuts import render
from .models import Product_proveedor
from django.shortcuts import redirect

# Create your views here.

def productos_list(request):
	product_list = Product_proveedor.getProductos()
	return render(request, 'productos/product_list.html',{ 'productos' : product_list})

def productos_create(request):
	get = request.GET
	proveedor_id = get['id_prov']
	tipo = get['tipo']
	familia = get['familia']
	tipo_id = get['id_tipo']
	proveedor_id = Product_proveedor.getProveedorId(proveedor_id)
	return render(request, 'productos/product_create.html', { 'prov_id' : proveedor_id, 'tipo': tipo, 'familia': familia, 'tipo_id': tipo_id })

def productos_insert(request):
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

	Product_proveedor.createProduct(producto_id, nombre, valor, tipo, prov_id)
	response = redirect('productos_list')
	return response

def productos_delete(request):
	get = request.GET
	product_id = get['id']
	Product_proveedor.deleteProduct(product_id)
	response = redirect('productos_list')
	return response

def productos_get(request):
	get = request.GET
	product_id = get['id']
	response = Product_proveedor.getProduct(product_id)
	return render(request, 'productos/product_update.html',{'product':response})

def productos_update(request):
	post = request.POST
	producto_id = post['producto_id']
	nombre = post['nombre']
	valor = post['valor']
	Product_proveedor.updateProduct(producto_id, nombre, valor)
	response = redirect('productos_list')
	return response



def familia_list(request):
	proveedor_list = Product_proveedor.getProveedores()
	familia_list = Product_proveedor.getFamilias()
	tipo_list = Product_proveedor.getTipos()
	return render(request, 'productos/family_type.html',{
		'familia' : familia_list,
		'tipo' : tipo_list,
		'proveedores' : proveedor_list
	})

def familia_create(request):
	post = request.POST
	proveedor_id = post['proveedor_id']
	return render(request, 'productos/family_create.html',{'proveedor':proveedor_id})

def familia_insert(request):
	post = request.POST
	identificador = post['identificador']
	detalle = post['detalle']
	id_proveedor = post['id_proveedor']
	Product_proveedor.createFamilia(identificador, detalle, id_proveedor)
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
	Product_proveedor.createTipo(identificador, detalle, id_familia)
	response = redirect('familia_list')
	return response
	